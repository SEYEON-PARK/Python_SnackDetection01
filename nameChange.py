# 사진 파일들 이름 바꾸기! 0000~쭉!
import os
   
folder = "C:/Users/april/Desktop/2023학년도 1학기/Python 프로젝트/snack01/pic05"

# 앞에 붙는 f는 포멧이고, 앞에 붙여줘야 한다.
for count, filename in enumerate(os.listdir(folder)): # 사진들이 리스트(?) 안에 들어있다.
    dst = f"{str(count+2817).zfill(4)}.jpg" # 이 이름으로 저장할 거다!
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder # 원래 이름 저장!
    dst =f"{folder}/{dst}" # 원하는 이름 저장!
        
    # rename() function will
    # rename all the files
    os.rename(src, dst) # 여기서 rename이라는 거는 경로 전체를 변경하는 거다!
    print("done") # 끝났음을 출력해주기!

'''
# 사진 파일들 이름 바꾸기! 0000~쭉!
import os
   
folder = "C:/Users/april/Desktop/2023학년도 1학기/Python 프로젝트/snack01/picSister"

# 앞에 붙는 f는 포멧이고, 앞에 붙여줘야 한다.
for count, filename in enumerate(os.listdir(folder)): # 사진들이 리스트(?) 안에 들어있다.
    dst = f"{str(count+2358).zfill(4)}.jpg" # 이 이름으로 저장할 거다!
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/{dst}"
        
    # rename() function will
    # rename all the files
    os.rename(src, dst) # 여기서 rename이라는 거는 경로 전체를 변경하는 거다!
    print("done")
'''


"""
# 사진 파일들 이름 바꾸기! 0000~쭉!
import os
   
folder = "C:/Users/april/Desktop/2023학년도 1학기/Python 프로젝트/snack01/picSister"

# 앞에 붙는 f는 포멧이고, 앞에 붙여줘야 한다.
for count, filename in enumerate(os.listdir(folder)): # 사진들이 리스트(?) 안에 들어있다.
    dst = f"{str(count+1709).zfill(4)}.jpg" # 이 이름으로 저장할 거다!
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/{dst}"
        
    # rename() function will
    # rename all the files
    os.rename(src, dst) # 여기서 rename이라는 거는 경로 전체를 변경하는 거다!
    print("done")

"""

"""
# 사진 파일들 이름 바꾸기! 0000~쭉!
import os
   
folder = "C:/Users/april/Desktop/2023학년도 1학기/Python 프로젝트/snack01/pic2"

# 앞에 붙는 f는 포멧이고, 앞에 붙여줘야 한다.
for count, filename in enumerate(os.listdir(folder)): # 사진들이 리스트(?) 안에 들어있다.
    dst = f"{str(count+461).zfill(4)}.jpg" # 이 이름으로 저장할 거다!
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/{dst}"
        
    # rename() function will
    # rename all the files
    os.rename(src, dst) # 여기서 rename이라는 거는 경로 전체를 변경하는 거다!
    print("done")
"""

'''
# 사진 파일들 이름 바꾸기! 0000~쭉!
import os
   
folder = "C:/Users/april/Desktop/2023학년도 1학기/Python 프로젝트/snack01/pic"

# 앞에 붙는 f는 포멧이고, 앞에 붙여줘야 한다.
for count, filename in enumerate(os.listdir(folder)): # 사진들이 리스트(?) 안에 들어있다.
    dst = f"{str(count).zfill(4)}.jpg" # 이 이름으로 저장할 거다!
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/{dst}"
        
    # rename() function will
    # rename all the files
    os.rename(src, dst) # 여기서 rename이라는 거는 경로 전체를 변경하는 거다!
    print("done")
'''

"""
# 사진 파일들 이름 바꾸기! 0~쭉!
import os
   
folder = "C:/Users/april/Desktop/2023학년도 1학기/Python 프로젝트/snack01/pic"

for count, filename in enumerate(os.listdir(folder)):
    dst = f"{str(count)}.jpg"
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/{dst}"
        
    # rename() function will
    # rename all the files
    os.rename(src, dst)
    print("done")
"""

'''
# 시작 폴더
sdir = ".\snack01_pictures"
# 도착 폴더
ddir = ".\snack01_pictures_result"

# 시작 폴더에서부터 PNG 파일을 다 읽어서
fileNames = Directory.GetFiles(sdir, "*.jpg", SearchOption.AllDirectories);
foreach (string file in fileNames)
{
    // 파일 이름만 따고
    string fileNameWithoutExtension = System.IO.Path.GetFileNameWithoutExtension(file).ToUpper();
    // 확장자 저장하고 (어차피 여기서는 png지만)
    string fileExtension = System.IO.Path.GetExtension(file);

    // List에 포함되어 있는 이름인지 확인 후
    if (contextList.ContainsKey(fileNameWithoutExtension).Equals(true))
    {
        // 새 이름을 생성하고
        string newFileName = fileNameWithoutExtension + "_new" + fileExtension;
        // 도착 폴더 경로와 합쳐
        string destFile = System.IO.Path.Combine(ddir, newFileName);
        // 파일 복사를 실행
        File.Copy(file, destFile, true);
    }
}
[출처] C# winform 특정 폴더에서 파일 읽어 이름 변경하고 복사하기|작성자 은기
'''
