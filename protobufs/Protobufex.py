import sample_pb2
sample_obj = sample_pb2.City()
sample_obj.name = 'Sumit'
sample_obj.pincode = '201306'
sample_obj.country = 'India'


samplelist = sample_obj.phone
samplelist.append('8197477794')
samplelist.append('8197477796')
print(sample_obj)
with open("file.bin","wb") as fo:
    bytesAsString = sample_obj.SerializeToString()
    fo.write(bytesAsString)
print("Reading from file")
with open("file.bin","rb") as fo:
    sample_obj_read = sample_pb2.City().FromString(fo.read())
    print(sample_obj_read)