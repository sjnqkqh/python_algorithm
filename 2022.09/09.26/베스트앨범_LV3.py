def solution(genres, plays):
    answer = []

    play_arr = []
    play_dict = dict()
    for i in range(len(genres)):
        play_arr.append((i, genres[i], plays[i]))

    # 장르별 재생횟수
    for item in play_arr:
        if play_dict.get(item[1]) is None:
            play_dict[item[1]] = item[2]
        else:
            play_dict[item[1]] += item[2]
    sorted_genre_arr = sorted(play_dict.items(), key=lambda x: (-x[1], x[0]))

    # 장르별로 최대 2곡 선정
    for sort in sorted_genre_arr:
        genre = sort[0]

        genre_music = []
        for item in play_arr:
            if item[1] == genre:
                genre_music.append(item)

        sorted_chart = sorted(genre_music, key=lambda x: (-x[2], x[0]))
        for i in range(min(len(sorted_chart), 2)):
            answer.append(sorted_chart[i][0])

    return answer
