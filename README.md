# run-py

## Introduction

When experimenting with keras models I always found it hard to keep track of all started runs and their results. 
Therefore I wrote this small helper repo.
The main idea is, if you start a run, it copies your python code and console output into a directory. 
You can then check later what actual code was running and which results where produced.

## Example

Let's make a run 'conv3d_run_copy.py' that contains a simple model:

```python
class Conv3DRun(SimpleRun):

    def _run(self, *arg, **kwargs) -> None:

        batch_size = ...
        train_data = ...

        model = Sequential([
            InputLayer(input_shape=(...)),
            Conv3D(32, 3, strides=2, activation='relu'),
            Conv3D(32, 3, strides=2, activation='relu'),
            GlobalAveragePooling3D(),
            Dropout(0.2),
            Dense(2, activation='softmax'),
        ])

        model.summary()
        model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
                 
        model.fit(
            train_data,
            ...,
            callbacks=[
                TensorBoard(log_dir=self.run_log_dir, batch_size=batch_size, write_graph=False),
                ModelCheckpoint(filepath=os.path.join(self.run_log_dir, 'checkpoint.hdf5')),
                ModelCheckpoint(filepath=os.path.join(self.run_log_dir, 'best_model.hdf5'), monitor='val_loss', verbose=0, save_best_only=True, save_weights_only=False, mode='auto', period=1),
            ],
        )


if __name__ == '__main__':
    Conv3DRun('/.../logs').run()
```

This would produce at '/.../logs' the folders 'Conv3DRun/2019_07_09_10_55_12' (with datetime=current datetime) with following files:
* output.txt: Containing the python console output
* conv3d_run_copy.py: Containing the above code.

and because we used self.run_log_dir for the keras callbacks it will also contain the checkpoint.hdf5 and best_model.hdf5 as well as the tensorboard files inside the given folder.
