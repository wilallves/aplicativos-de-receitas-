CREATE DATABASE cadastro_usuarios;
USE cadastro_usuarios;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    celular VARCHAR(20) NOT NULL,
    senha VARCHAR(100) NOT NULL
);

INSERT INTO usuarios (nome, email, celular, senha)
VALUES ('Nome do Usuário', 'exemplo@email.com', '123456789', 'senha123');

        
        top_layout.add_widget(BoxLayout())

        
        top_layout.add_widget(ingredient_label)

        
        main_layout.add_widget(top_layout)
        main_layout.add_widget(bottom_layout)
        
        return main_layout
    
class MinhaApp(App):
    def build(self):
        return Image(source='/Users/aluno.sesipaulista/Downloads/lasanha.sos.jpg')

if __name__ == '__main__':
    RecipeApp().run()
