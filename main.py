import praw


def get_username(reddit_object):
    username = reddit_object.user.me()
    return username


def get_all_comments(r):
    username = get_username(r)
    comments = r.redditor(str(username)).comments.new()
    list_of_comments = []
    for comment in comments:
        list_of_comments.append({"comment_id": comment.id,
                                 "comment_body": comment.body,
                                 "comment_permalink": comment.permalink})
    return list_of_comments


def delete_all_comments(r):
    comments = get_all_comments(r)

    if len(comments) == 0: return print("No comments found")

    for comment in comments:
        try:
            r.comment(comment["comment_id"]).delete()
        except:
            print("Could not delete comment: " + comment["comment_id"])

    print(f"Successfully deleted {len(comments)} comments.")


def edit_and_delete_all_comments(r):
    comments = get_all_comments(r)
    if len(comments) == 0: return print("No comments found")

    for comment in comments:
        try:
            r.comment(comment["comment_id"]).edit("Lorem Ipsum...")
            r.comment(comment["comment_id"]).delete()
        except:
            print("Could not edit and delete comment: " + comment["comment_id"])

    print(f"Successfully edited and deleted {len(comments)} comments.")


def show_all_comments(r):
    comments = get_all_comments(r)
    for comment in comments:
        print("Comment ID: " + comment["comment_id"])
        print("Comment Body: " + comment["comment_body"])
        print("Comment Link: " + comment["comment_permalink"])
        print("------------------")

    print(f"Found {len(comments)} comments")


def main():
    r = praw.Reddit("SCRIPT")
    r.validate_on_submit = True

    print("Reddit Nuker")
    print("1. Show all comments")
    print("2. Delete all comments")
    print("3. Edit and delete all comments")

    menu_choice = input("Choose a number (1-5):")
    if menu_choice == 1 or menu_choice == "1":
        show_all_comments(r)
    elif menu_choice == 2 or menu_choice == "2":
        delete_all_comments(r)
    elif menu_choice == 3 or menu_choice == "3":
        edit_and_delete_all_comments(r)


if __name__ == '__main__':
    main()
