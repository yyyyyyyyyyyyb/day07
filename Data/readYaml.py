import yaml
with open("./data1.yaml","r")as f :
    data=yaml.safe_load(f)
    print("返回字典数据：",data)
    print("返回字典数据：",type(data))