from project.config.Database import connection
from flask import jsonify
import pandas as pd
import json

import os
from imageai.Detection import ObjectDetection
from imageai.Detection import VideoObjectDetection
import requests
import cv2
import shutil

path = os.getcwd()
parent = os.path.dirname(path) 
image_path = os.path.join(parent,'Mobilaty\\project\\public\\temp.jpeg')
Base_Video_path = os.path.join(parent , 'Mobilaty\\project\\public')

counter = 0
input_video = ""
y=0
def forFrame(frame_number, output_array, output_count):
    objs = ""
    print("FOR FRAME " , frame_number)
    print("Output for each object : ", output_array)
    global y 
    #print(str(y) + '  ' + str(len(output_array))+'\n')
    cap = cv2.VideoCapture(os.path.join(Base_Video_path, input_video))
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh:"+input_video)
    for output in output_array:
        objs+=output["name"] + " : " + str(output["percentage_probability"])
    if(y!=len(output_array)):
        cap.set(1,frame_number); # Where frame_no is the frame you want
        ret, frame = cap.read() # Read the frame
        for obj in output_array:
            bbox = obj["box_points"]
            crop_img = frame[int(bbox[1]):int(bbox[3]),int(bbox[0]):int(bbox[2])]
            try:
                cv2.imwrite(os.path.join(Base_Video_path, str(counter)+"new.jpg"), crop_img)
            except:
                print('------------------------------------error')
        y=len(output_array)
    print("Output count for unique objects : ", output_count)
    print(objs)

    print("------------END OF A FRAME --------------")

class Mobile:

    def __init__(self):
        self.conn = connection()
        self.cursor = self.conn.connection.cursor(dictionary=True)

    def add_mobile(self, params):
        val = "'{}'".format(params['mobile_id'])
        val2 = "'{}'".format(params['cat_id'])
        self.cursor.execute("INSERT INTO mobilaty.mobile" +
                            " (mobile_id , mobile_name ,cat_id,display_size,main_camera,selfie_camera,chipset,storage_and_ram,battary,price)" +
                            " VALUES (" + val + ",'" + params['mobile_name'] +
                            "'," + val2+ ",'" + params['display_size'] + "','" + params['main_camera']
                           + "','" + params['selfie_camera'] + "','" + params['chipset'] + "','" + params['storage_and_ram']
                           + "','" + params['battary'] + "','" + params['price']+ "')")
        self.conn.connection.commit()

    def delete_mobile(self, params):
        val = "'{}'".format(params['mobile_id'])
        self.cursor.execute('DELETE FROM  mobilaty.mobile WHERE mobile_id= ' +val)
        self.conn.connection.commit()
        # row = cursor.fetchone()

    def show_AllMobile(self):
        self.cursor.execute('SELECT * FROM mobilaty.mobile')
        row = self.cursor.fetchall()
        return row

    def update_mobile(self, params):
        val = "'{}'".format(params['mobile_id'])
        val2 = "'{}'".format(params['cat_id'])
        self.cursor.execute("update mobilaty.mobile set mobile_name = '" +
                            params['mobile_name'] + "'and cat_id= " +
                            params['cat_id'] +
                            + " and display_size= '" + params['display_size'] 
                            + "'and main_camera= '" + params['main_camera']
                            + "'and selfie_camera= '" + params['selfie_camera']
                            + "'and chipset= '" + params['chipset']
                            + "'and storage_and_ram= '" + params['storage_and_ram']
                            + "'and battary= '" + params['battary']
                            + "'and price= '" + params['price']+ "' where mobile_id = " + val)
        self.conn.connection.commit()

    def show_mobile(self, params):
        val = "'{}'".format(params['mobile_id'])
        self.cursor.execute('SELECT * FROM mobilaty.mobile WHERE mobile_id = ' + val + " ORDER BY RAND()")
        row = self.cursor.fetchall()
        return row

    def findByMobileId(self, params):
        val = "'{}'".format(params['mobile_id'])
        self.cursor.execute('SELECT * FROM mobilaty.mobile WHERE mobile_id = ' + val)
        row = self.cursor.fetchall()
        return row

    def getimage(self,params):
        image_url = params['url']
        print("hrrrrrrrrrrrrrrrrrrrrrrr::::::",image_url)
        try:
            # Open the url image, set stream to True, this will return the stream content.
            resp = requests.get(image_url, stream=True)
            # Open a local file with wb ( write binary ) permission.
            local_file = open(image_path, 'wb')
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            resp.raw.decode_content = True
            # Copy the response stream raw data to local image file.
            shutil.copyfileobj(resp.raw, local_file)
            # Remove the image url response object.
            del resp
            return cv2.imread(image_path)
        except:
            return str("Error in get image")


    def Crop_image(self,params):
        url = ""
        if 'url' in params.keys():
            url = params['url']
            print("herrrrrrrrrrrrrrrrrrrrrrrrr:",url)
        else:
            return "Error: No url field provided. Please specify an url."
        im = self.getimage(params)
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath(os.path.join(parent,'Mobilaty\\project\\public\\resnet50_coco_best_v2.0.1.h5'))
        detector.loadModel()
        custom_objects = detector.CustomObjects(cell_phone=True)
        detections = detector.detectCustomObjectsFromImage(input_image=image_path,
                                                                output_image_path=os.path.join(parent,'Mobilaty\\project\\public\\result.jpeg'),
                                                                custom_objects=custom_objects, minimum_percentage_probability=50)
        
        objs = ""
        counter = 0
        for eachObject in detections:
            objs+=eachObject["name"] + " : " + str(eachObject["percentage_probability"])
            print(eachObject["name"] + " : " + str(eachObject["percentage_probability"]))
            
            bbox = eachObject["box_points"]
            crop_img = im[int(bbox[1]):int(bbox[3]),int(bbox[0]):int(bbox[2])]
            try:
                cv2.imwrite(os.path.join(parent,'Mobilaty\\project\\public\\'+str(counter)+"image.jpg"), crop_img)
                #main(str(os.path.join(execution_path ,str(counter)+"image.jpg")))
            except:
                return str("Error in write")

            counter+=1
        os.remove(image_path)
        os.remove(os.path.join(parent,'Mobilaty\\project\\public\\result.jpeg'))
        return str(objs)
    

    def Crop_video(self,params):
        global input_video 
        
        if 'videoName' in params.keys():
            input_video = str(params['videoName'])
            print(input_video)
        else:
            return "Error: No Video Name field provided. Please specify an url."
        detector = VideoObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath(os.path.join(parent,'Mobilaty\\project\\public\\yolo.h5'))
        detector.loadModel()
        custom_objects = detector.CustomObjects(cell_phone=True)
        
        
        video_path = detector.detectCustomObjectsFromVideo(
                        custom_objects=custom_objects,
                        input_file_path=os.path.join(Base_Video_path, input_video),
                        output_file_path=os.path.join(Base_Video_path, "traffic_custom_detected"),
                        save_detected_video=False,
                        frames_per_second=1,
                        per_frame_function=forFrame)
        os.remove(os.path.join(Base_Video_path, "traffic_custom_detected"))
        return "Done!"
    

    def recommendations(self,params,cosine_sim):
        
        dataset = pd.read_csv(os.path.join(parent,'Mobilaty\\project\\public\\Data_ExcelM.csv'))
        indices = pd.Series(dataset.index)
        # initializing the empty list of recommended movies
        recommended_movies = []
        cosine_sim = cosine_sim
        # gettin the index of the movie that matches the title    
        idx = indices[indices == params['title']].index[0]
        #print("heeeeeeeeeeeeeeeeeeeee:",idx)
        # creating a Series with the similarity scores in descending order
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
        #print("heeeeeeeeeeeeeeeeeeeee:",indices[indices == title].index[0])
        # getting the indexes of the 10 most similar movies
        top_n_indexes = list(score_series.iloc[1:params['num']+1].index)
        #print("------------------------------------------------------")
        #print("heeeeeeeeeeeeeeeeeeeeexxxxxxxxxxxxxxxxxx:",top_n_indexes)
        #print("------------------------------------------------------")
        
        # populating the list with the titles of the best 10 matching movies
        for i in top_n_indexes:
            recommended_movies.append(list(dataset.index)[i])
        
        result = []
        for ii in range(len(recommended_movies)):
            result.append(dataset.iloc[recommended_movies[ii]].values)
        result = pd.Series(result).to_json(orient='values')
        return result
