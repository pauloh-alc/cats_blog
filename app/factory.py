from app.models import TextPost, ImagePost


class PostFactory:
    @staticmethod
    def create_post(title, body, path_image, author_id):
        post_type = "image" if path_image.endswith(('.jpg', '.jpeg', '.png')) else "text"

        if post_type == 'text':
            return TextPost(title=title, body=body, author_id=author_id)
        elif post_type == 'image':
            return ImagePost(title=title, body=body, author_id=author_id, path_image=path_image)
        else:
            raise ValueError(f"Tipo desconhecido: {post_type}")