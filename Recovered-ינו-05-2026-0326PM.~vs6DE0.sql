use master
go

create database RecipeDB collate hebrew_100_ci_as
use RecipeDB
go

CREATE TABLE categories (
    category_id INT IDENTITY(1,1) NOT NULL,
    category_name VARCHAR(50) NOT NULL,
    CONSTRAINT PK_categories PRIMARY KEY(category_id)
)

CREATE TABLE users (
    user_id INT IDENTITY(1,1) NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NULL,
    CONSTRAINT PK_users PRIMARY KEY(user_id)
)

CREATE TABLE recipes (
    recipe_id INT IDENTITY(1,1) NOT NULL,
    recipe_name VARCHAR(100) NOT NULL,
    instructions TEXT NOT NULL,
    category_id INT NOT NULL,
    user_id INT NOT NULL,
    CONSTRAINT PK_recipes PRIMARY KEY(recipe_id),
    CONSTRAINT FK_recipes_categories FOREIGN KEY (category_id) REFERENCES categories(category_id),
    CONSTRAINT FK_recipes_users FOREIGN KEY (user_id) REFERENCES users(user_id)
)

CREATE TABLE ingredients (
    ingredient_id INT IDENTITY(1,1) NOT NULL,
    ingredient_name VARCHAR(100) NOT NULL,
    CONSTRAINT PK_ingredients PRIMARY KEY(ingredient_id)
)

-- 5. טבלת קישור: מרכיבים לכל מתכון (טבלת ה-Many-to-Many)
CREATE TABLE recipe_ingredients (
    recipe_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    amount VARCHAR(50) NOT NULL, -- למשל: "2 כוסות"
    CONSTRAINT PK_recipe_ingredients PRIMARY KEY(recipe_id, ingredient_id),
    CONSTRAINT FK_ri_recipes FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id),
    CONSTRAINT FK_ri_ingredients FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)
)

INSERT INTO categories (category_name)
VALUES
(N'קינוחים'),
(N'מנות עיקריות'),
(N'סלטים'),
(N'מאפים'),
(N'טבעוני');

INSERT INTO users (username, email)
VALUES
(N'אורן', 'oren@gmail.com'),
(N'דנה', 'dana@gmail.com'),
(N'יוסי', 'yossi@gmail.com');


INSERT INTO recipes (recipe_name, instructions, category_id, user_id)
VALUES
(
    N'עוגת שוקולד',
    N'לערבב את כל החומרים, לאפות ב-180 מעלות כ-40 דקות.',
    1, -- קינוחים
    1  -- אורן
),
(
    N'סלט ירקות ישראלי',
    N'לחתוך ירקות, להוסיף שמן זית, לימון ומלח.',
    3, -- סלטים
    2  -- דנה
),
(
    N'פסטה ברוטב עגבניות',
    N'לבשל פסטה, להכין רוטב עגבניות ולערבב יחד.',
    2, -- מנות עיקריות
    3  -- יוסי
);

INSERT INTO ingredients (ingredient_name)
VALUES
(N'קמח'),
(N'סוכר'),
(N'שוקולד'),
(N'ביצים'),
(N'עגבניות'),
(N'מלפפון'),
(N'בצל'),
(N'פסטה'),
(N'שמן זית'),
(N'מלח');

-- עוגת שוקולד (recipe_id = 1)
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount)
VALUES
(1, 1, N'2 כוסות'),   -- קמח
(1, 2, N'1 כוס'),     -- סוכר
(1, 3, N'200 גרם'),   -- שוקולד
(1, 4, N'3 יחידות'); -- ביצים

-- סלט ירקות (recipe_id = 2)
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount)
VALUES
(2, 5, N'2 יחידות'),  -- עגבניות
(2, 6, N'2 יחידות'),  -- מלפפון
(2, 7, N'1 יחידה'),   -- בצל
(2, 9, N'2 כפות'),    -- שמן זית
(2, 10, N'לפי הטעם'); -- מלח

-- פסטה (recipe_id = 3)
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount)
VALUES
(3, 8, N'500 גרם'),   -- פסטה
(3, 5, N'4 יחידות'),  -- עגבניות
(3, 9, N'3 כפות'),    -- שמן זית
(3, 10, N'לפי הטעם'); -- מלח
