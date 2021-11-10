
if __name__ == "__main__":
    import torch

    print(torch.cuda.is_available())

    if torch.cuda.is_available():
        print(torch.cuda.current_device())
        print(torch.cuda.device(0))
        print(torch.cuda.get_device_name(0))
