# https://www.reddit.com/r/dailyprogrammer/comments/wjzly/7132012_challenge_76_easy_title_case/

def titlecase(input, exception):
    words = input.split()
    output = [words[0].title()]
    for word in words[1:]:
        if word.lower() in exception:
            output.append(word.lower())
        else:
            output.append(word.title())
    return ' '.join(output)

print(titlecase("This is a hard one", "hard"))