
import os

import shutil



def organize_files(directory_path):

    # Create a dictionary to store file extensions and their corresponding directories

    file_types = {}



    # Iterate through all files in the directory

    for filename in os.listdir(directory_path):

        if os.path.isfile(os.path.join(directory_path, filename)):

            # Extract the file extension

            file_extension = filename.split('.')[-1]



            # If the file extension is not in the dictionary, add it with a new directory

            if file_extension not in file_types:

                file_types[file_extension] = os.path.join(directory_path, file_extension)



                # Create the directory if it doesn't exist

                os.makedirs(file_types[file_extension], exist_ok=True)



            # Move the file to the corresponding directory

            shutil.move(

                os.path.join(directory_path, filename),

                os.path.join(file_types[file_extension], filename)

            )



    print("Files organized successfully!")



# Specify the directory path you want to organize

directory_to_organize = "/path/to/your/directory"



# Call the function to organize files

organize_files(directory_to_organize)



