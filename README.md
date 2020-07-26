# Image-sorter

With this program you can randomly collect images upto a specified limit from the mentioned directories and collect them to a user specified folder

``` Python
actress_list=[b'E:\New folder\Kareena Kapoor',b'E:\New folder\Shraddha Kapoor',b'E:\New folder\Sonakshi Sinha']
```
In the above syntax you have to put the source destination of the folder from which you want to collect.


REMEMBER TO PUT b INFORNT OF EVERY LIST ELEMENT TO CONVERT IT TO BYTE FORMAT BECAUSE THE COMPILER CANNOT PROCESS THE UNICODE ENCODING.

``` Python

python image_sorter.py "USER DEFINED FOLDER NAME WHERE YOU WANT TO STORE THE PICTURES OR DATA"

```

While compiling via the cmd make sure to specify the folder name or else ot will throw and System_argument exception
And also do not make two directories with same name.

 
 ``` Python 
        for i in range(1,25):
        sorted_list.append(list[random.randrange(0,list_length)])
 ```
 
 Increase the range value to pick the more random images data .
 
 ##Enjoy 
