# Imports
import praw

# Init Reddit client
r = praw.Reddit("SCRIPT")
r.validate_on_submit = True


def get_username():
    username = r.user.me()
    return username


def get_all_comments():
    username = get_username()
    comments = r.redditor(str(username)).comments.new()
    list_of_comments = []
    for comment in comments:
        list_of_comments.append(
            {
                "comment_id": comment.id,
                "comment_body": comment.body,
                "comment_permalink": comment.permalink,
            }
        )
    return list_of_comments


def edit_and_delete_all_comments():
    comments = get_all_comments()
    if len(comments) == 0:
        return print("No comments found")

    for comment in comments:
        try:
            print("Editing and Deleting comment: " + comment["comment_id"])
            edit_comment(comment["comment_id"])
            delete_comment(comment["comment_id"])
        except:
            print("Could not edit and delete comment: " + comment["comment_id"])
            return

    print(f"Successfully edited and deleted {len(comments)} comments.")


def show_all_comments():
    comments = get_all_comments()
    for comment in comments:
        print("Comment ID: " + comment["comment_id"])
        print("Comment Body: " + comment["comment_body"])
        print("Comment Link: " + comment["comment_permalink"])
        print("------------------")

    print(f"Found {len(comments)} comments")


def delete_comment(comment: str):
    try:
        r.comment(comment).delete()
    except:
        print("Could not delete comment: " + comment)
        return


def edit_comment(comment: str):
    try:
        r.comment(comment).edit(body="Lorem Ipsum...")
    except:
        print("Could not edit comment: " + comment)
        return


def main():
    print("Reddit Nuker")
    print("1. Show all comments")
    print("2. Edit and delete all comments")

    menu_choice = input("Choose a number (1-2):")
    if menu_choice == 1 or menu_choice == "1":
        show_all_comments()
    elif menu_choice == 2 or menu_choice == "2":
        edit_and_delete_all_comments(r)
    else:
        print("You should press the correct button :)")


if __name__ == "__main__":
    main()
