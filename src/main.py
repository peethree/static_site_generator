from generate_page_recursively import generate_page_recursively, dig_for_files
import os
import shutil


def main():
    # delete public if it exists
    if os.path.exists("public"):
        print("Deleting public directory . . .")
        shutil.rmtree("public")      

    if os.path.exists("static"):
        # get the files in static
        list_of_paths = dig_for_files("static")       

        # copy over static files to public
        for path in list_of_paths:     
            relative_path = os.path.relpath(path, "static")               
            destination_path = os.path.join("public", relative_path)

            # make directories if they don't exist (public, public/images/)
            os.makedirs(os.path.dirname(destination_path))  
            print("Copying files do public directory . . .")              
            shutil.copy(path, destination_path)

    # Generate pages from content/ dir, using template.html and write it to public/ dir   
    generate_page_recursively("./content/", "template.html", "./public/")


if __name__ == "__main__":
    main()