import subprocess


def upload(s3_bucket_name=None, mlruns_direc=None):
    try:
        output = subprocess.run(["aws",  "s3", "sync", "{}".format(mlruns_direc),
                                 "s3://{}".format(s3_bucket_name)],
                                stdout=subprocess.PIPE,
                                encoding='utf-8')

        print("\nSaved to bucket: ", s3_bucket_name)
        return f"Done Uploading : {output.stdout}"

    except Exception as e:
        return f"Error Occurred While Uploading : {e.__str__()}"
