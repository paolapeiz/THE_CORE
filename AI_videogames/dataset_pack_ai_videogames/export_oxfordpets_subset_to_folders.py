"""Exporta un subconjunto de Oxford-IIIT Pet a carpetas.

Salida:
data_pets_subset/
  train/<label_name>/*.jpg
  test/<label_name>/*.jpg
"""

import os
import tensorflow as tf
import tensorflow_datasets as tfds

OUT_DIR = os.environ.get("OUT_DIR", "data_pets_subset")
IMG_SIZE = int(os.environ.get("IMG_SIZE", "160"))
MAX_TRAIN = int(os.environ.get("MAX_TRAIN", "400"))
MAX_TEST = int(os.environ.get("MAX_TEST", "120"))

(ds_train, ds_test), info = tfds.load(
    "oxford_iiit_pet",
    split=["train[:80%]", "train[80%:]"],
    with_info=True,
    as_supervised=True
)

label_names = info.features["label"].names

def save_example(image, label, split_name, idx):
    label_name = label_names[int(label)]
    cls_dir = os.path.join(OUT_DIR, split_name, label_name)
    os.makedirs(cls_dir, exist_ok=True)
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    image = tf.cast(image, tf.uint8)
    tf.keras.utils.save_img(os.path.join(cls_dir, f"{split_name}_{idx:05d}.jpg"), image)

for i, (image, label) in enumerate(ds_train.take(MAX_TRAIN)):
    save_example(image, label, "train", i)

for i, (image, label) in enumerate(ds_test.take(MAX_TEST)):
    save_example(image, label, "test", i)

print("Export completado en:", OUT_DIR)