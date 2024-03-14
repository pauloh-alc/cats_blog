USE cats_blog;

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    cat_name VARCHAR(50) NOT NULL,
    cat_sex CHAR(1) NOT NULL
);

CREATE TABLE IF NOT EXISTS post (
	id INT AUTO_INCREMENT PRIMARY KEY,
    path_image VARCHAR(512) NOT NULL,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES user(id)
);

-- Inserindo dados na tabela 'user'
INSERT INTO user (user_name, password, cat_name, cat_sex) VALUES
('usuario1', 'senha123', 'Mimi', 'F'),
('usuario2', 'senha456', 'Felix', 'M'),
('usuario3', 'senha789', 'Luna', 'F');

-- Inserindo dados na tabela 'post'
INSERT INTO post (path_image, title, body, author_id) VALUES
('/caminho/para/imagem1.jpg', 'Título do Post 1', 'Conteúdo do Post 1', 1),
('/caminho/para/imagem2.jpg', 'Título do Post 2', 'Conteúdo do Post 2', 2),
('/caminho/para/imagem3.jpg', 'Título do Post 3', 'Conteúdo do Post 3', 3);


SELECT * FROM cats_blog.user;
SELECT * FROM cats_blog.post;

SELECT * FROM cats_blog.user u 
INNER JOIN cats_blog.post p ON p.author_id = u.id;

DROP TABLE post;
DROP TABLE user;

DELETE FROM cats_blog.user
WHERE id IN (SELECT concat("'",id,"'") FROM cats_blog.user);

SELECT concat("'",id,"'") FROM cats_blog.user;

ALTER TABLE cats_blog.user MODIFY password VARCHAR(180);

UPDATE  cats_blog.user 
SET cat_sex = 'F'
where id = 15;
