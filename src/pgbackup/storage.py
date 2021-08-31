def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()
def s3(client, infile, bucket_name, file_name):
    client.upload_fileobj(infile, bucket_name, file_name)
