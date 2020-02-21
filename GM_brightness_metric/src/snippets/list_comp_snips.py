total_frames = 146
current_frame = iter(list(range(1, total_frames+1, 1)))
for i in current_frame:
    print(next(current_frame))

#gm_value_dict = (lambda frame: {next(current_frame)