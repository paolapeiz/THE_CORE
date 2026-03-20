import tensorflow_datasets as tfds

(ds_train, ds_test), info = tfds.load(
    "oxford_iiit_pet",
    split=["train[:80%]", "train[80%:]"],
    with_info=True,
    as_supervised=True
)

print(info)
print("Dataset descargado y preparado correctamente.")