import logging
import threading
import os
import darknet

OBJ_DATA = os.getenv("OBJ_DATA", "/app/object-detection/obj.data")
YOLOV3 = os.getenv("YOLOV3", "/app/object-detection/yolov3.cfg")
WEIGHTS = os.getenv("WEIGHTS", "/app/object-detection/backup/yolov3_last.weights")

class DarknetManager:

    init_number_of_instances = 16

    instances = []
    instances_lock = threading.Lock()

    @classmethod
    def prepare_instances(cls):
        cls.instances = []
        for _ in range(cls.init_number_of_instances):
            cls.instances.append(Darknet()) 

        logging.info("Darknet instances created")


    @classmethod
    def get_available_instance(cls):
        with cls.instances_lock:
            i = 0

            for instance in cls.instances:
                if instance.available:
                    instance.available = False
                    logging.info(f"Instance {i} in use")
                    return instance  
                
                i = i + 1

            instance = Darknet()
            instance.available = False 
            cls.instances.append(instance)
            logging.info("New Darknet instance created")

            return instance  


    @classmethod
    def release_instance(cls, instance):
        if instance in cls.instances:
            if not instance.available:  
                logging.info('Darknet instance released')
                instance.available = True  
            else:
                logging.warning('Instansce is already released')
        else:
            logging.error('Instance not found in the instances list')

 
class Darknet: 
  def __init__(self):
      cfg_file = YOLOV3
      names_file = OBJ_DATA
      weights_file = WEIGHTS

      # First thing we do is load the neural network.
      self.network, self.class_names, self.colours, self.metadata = darknet.load_network(cfg_file, names_file,
                                                                                         weights_file)
      self.width = darknet.network_width(self.network)
      self.height = darknet.network_height(self.network)

      self.prediction_threshold = 0.25

      self.available = True

  def process(self, image):
      darknet_image = darknet.convert_cv2_image2darknet_image(image)
      resized_image = darknet.resize_image(darknet_image, self.width, self.height)

      detections = darknet.detect_image(self.network, self.class_names, resized_image,
                                        darknet.ImageDimension(width=darknet_image.w, height=darknet_image.h),
                                        thresh=self.prediction_threshold)

      darknet.free_image(darknet_image)
      darknet.free_image(resized_image)

      return detections
