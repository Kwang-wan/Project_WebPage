# roof DB





table tag

| 필드명  | 타입        | 제약 조건          | 설명      |
| ------- | ----------- | ------------------ | --------- |
| tag_id  | Integer     | PK, Auto Increment | 기본 키   |
| title   | varchar(10) | not null           | 태그 이름 |
| content | text        | not null           | 설명      |



table category

| 필드명      | 타입        | 제약 조건          | 설명          |
| ----------- | ----------- | ------------------ | ------------- |
| category_id | Integer     | PK, Auto Increment | 기본 키       |
| title       | varchar(10) | not null           | 카테고리 이름 |
| content     | text        | not null           | 설명          |



table member

| 필드명    | 타입        | 제약 조건          | 설명      |
| --------- | ----------- | ------------------ | --------- |
| member_id | Integer     | PK, Auto Increment | 기본 키   |
| name      | varchar(10) | not null           | 멤버 이름 |



table post

| 필드명         | 타입        | 제약 조건          | 설명                 |
| -------------- | ----------- | ------------------ | -------------------- |
| post_id        | Integer     | PK, Auto Increment | 기본 키, 게시글 번호 |
| title          | varchar(25) | not null           | 제목                 |
| content        | text        |                    | 게시글 소개          |
| photo_id1      | Integer     | FK                 | 사진, 여러장         |
| photo_id2      | Integer     | FK                 | 사진, 여러장         |
| photo_id3      | Integer     | FK                 | 사진, 여러장         |
| photo_id4      | Integer     | FK                 | 사진, 여러장         |
| photo_id5      | Integer     | FK                 | 사진, 여러장         |
| photo_id6      | Integer     | FK                 | 사진, 여러장         |
| photo_id7      | Integer     | FK                 | 사진, 여러장         |
| photo_id8      | Integer     | FK                 | 사진, 여러장         |
| photo_id9      | Integer     | FK                 | 사진, 여러장         |
| photo_id10     | Integer     | FK                 | 사진, 여러장         |
| date           | datetime    | not null           | 작성일               |
| category_title | varchar(10) | FK                 | 카테고리 이름        |
| member_id      | Integer     | FK                 | 작성자 아이디        |
| tag_id1        | Integer     | FK                 | 태그                 |
| tag_id2        | Integer     | FK                 | 태그                 |
| tag_id3        | Integer     | FK                 | 태그                 |
| tag_id4        | Integer     | FK                 | 태그                 |
| tag_id5        | Integer     | FK                 | 태그                 |



table photo

| 필드명    | 타입         | 제약 조건          | 설명               |
| --------- | ------------ | ------------------ | ------------------ |
| photo_id  | Integer      | PK, Auto Increment | 기본 키, 사진 번호 |
| title     | varchar(25)  | not null           | 이름               |
| source    | varchar(200) |                    | 사진 경로          |
| member_id | Integer      | FK                 | 멤버               |
| post_id   | Integer      | FK                 | 게시글 번호        |
| content   | text         |                    | 사진 설명          |



