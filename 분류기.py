import os
import shutil
from datetime import datetime

def organize_files_by_creation_date(source_dir):
    # 디렉토리 존재 여부 확인
    if not os.path.isdir(source_dir):
        print(f"지정한 경로가 디렉토리가 아닙니다: {source_dir}")
        return

    # source_dir 내 파일들을 순회
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)

        # 파일만 처리 (디렉토리는 제외)
        if os.path.isfile(file_path):
            # 파일의 생성시간 가져오기 (Unix는 ctime이 변경시간일 수 있음에 유의)
            creation_time = os.path.getctime(file_path)
            creation_date = datetime.fromtimestamp(creation_time)
            folder_name = creation_date.strftime("%m_%d")

            # 이동 대상 폴더 경로 생성
            target_folder = os.path.join(source_dir, folder_name)
            os.makedirs(target_folder, exist_ok=True)

            # 파일 이동
            shutil.move(file_path, os.path.join(target_folder, file_name))
            print(f"Moved: {file_name} → {folder_name}/")

# 사용 예시
if __name__ == "__main__":
    source_directory = "./2025_06"  # 경로 수정 필요
    organize_files_by_creation_date(source_directory)
