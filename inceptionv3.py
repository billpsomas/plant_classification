from tensorflow.keras.layers import Dense, Dropout

import tensorflow as tf

def InceptionV3(height, width, num_classes):

     base = tf.keras.applications.InceptionV3(pooling='avg',
                                             weights='imagenet', 
                                             include_top = False, 
                                             input_shape=(height,width,3), 
                                             classes=num_classes)
     
     name = InceptionV3.__name__

     x = base.output
     x = tf.keras.layers.Dense(2048, activation='relu', name='fc2048')(x)
     x = tf.keras.layers.Dropout(0.5)(x)
     x = tf.keras.layers.Dense(num_classes, activation='softmax', name='fc' + str(num_classes))(x)
     model = tf.keras.Model(base.input, x, name = 'nasnetmobile')

     return model, name