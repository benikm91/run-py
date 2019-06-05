import os


def restrict_gpus(gpu: int, *gpus: int):

    def curry():
        os.environ["CUDA_VISIBLE_DEVICES"] = ','.join(*([gpu] + list(gpus)))

    return curry
