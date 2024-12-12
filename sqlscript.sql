create database rough


use rough


CREATE TABLE article (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE comment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    articleId INT NOT NULL,
    message TEXT NOT NULL,
    FOREIGN KEY (articleId) REFERENCES article(id) ON DELETE CASCADE
);

INSERT INTO article (title, content) VALUES
('The Future of AI', 'Artificial Intelligence is transforming the world at an incredible pace.'),
('Climate Change Effects', 'Global warming is leading to rising sea levels and extreme weather patterns.'),
('The Rise of Quantum Computing', 'Quantum computers have the potential to solve problems that are intractable for classical computers.'),
('Space Exploration Advances', 'Space agencies are planning missions to Mars and beyond.'),
('Renewable Energy Growth', 'Solar and wind energy are becoming more efficient and widespread.');


