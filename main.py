import praw


def get_username(reddit_object):
    username = reddit_object.user.me()
    return username


def get_all_comments(r):
    username = get_username(r)
    return r.redditor(str(username)).comments.new()


def delete_all_comments(r, comment_ids):
    if len(comment_ids) == 0: return print("No comments found")

    # Will try to delete all comments in list.
    try:
        for comment in comment_ids:
            r.comment(comment).delete()
    except:
        print(f"Could not delete comment: {comment_ids}")
        return

    print(f"Successfully deleted {len(comment_ids)} comments.")


def edit_and_delete_all_comments(r, comment_ids):
    if len(comment_ids) == 0: return print("No comments found")

    # Will try to edit and delete all comments in list
    for comment in comment_ids:
        try:
            r.comment(comment).edit("Lorem ipsum...")
            r.comment(comment).delete()
        except:
            print(f"Could not edit and delete comment: {comment}")
            return

    print(f"Successfully edited and deleted {len(comment_ids)} comments.")


def show_all_comments(r):
    comments = get_all_comments(r)
    count = 0
    for comment in comments:
        count += 1
        print("------------------")
        print(f"Comment ID: {comment.id}")
        print(f"Comment Text: {comment.body}")
        print(f"Comment Link: https://reddit.com{comment.permalink}")

    print("------------------")
    print(f"Found {count} comments.")


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
        comments = []
        delete_all_comments(r, comments)
    elif menu_choice == 3 or menu_choice == "3":
        edit_and_delete_all_comments(r)


if __name__ == '__main__':
    main()
