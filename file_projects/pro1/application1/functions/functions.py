def handle_upload_file(file):
    with open('application1/static/upload_files/'+file, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
