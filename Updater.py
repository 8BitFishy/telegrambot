import os
import time
import shutil

with open("logs.txt", "w") as f:
    f.write("Trying to delete main file: \n")
    dir = "wollybot-main"
    print("Updating...")
    time.sleep(5)
    try:
        f.write(f"Trying to remove {dir}")

        shutil.rmtree(dir)
        '''
        for file in os.listdir(dir):
            print(f"Trying to remove {file}")
            os.remove(os.path.join(dir, file))
        '''
        f.write(f"{dir} removed")

    except Exception as e:
        print(f"Failed with error {e}")
        f.write(str(e))

    f.write("\nTrying to rename files: \n")

    try:
        os.replace("Update_Files", "wollybot-main")
    except Exception as e:
        f.write(str(e))
        print(f"Failed renaming with error {e}")

update_file_dir = "Update_Files"

if os.path.exists(update_file_dir):
    shutil.rmtree(update_file_dir)


#os.execv(sys.argv[0], sys.argv)
