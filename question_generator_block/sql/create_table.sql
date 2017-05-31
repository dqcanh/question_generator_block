CREATE TABLE edxapp.qgb_question_template (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	xblock_id VARCHAR(255) NOT NULL UNIQUE,
	template VARCHAR(8192) NOT NULL,
	url_image VARCHAR(8192) NOT NULL,
	resolver VARCHAR(255) NOT NULL,
	answer_template VARCHAR(8192) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci AUTO_INCREMENT=40;

CREATE TABLE edxapp.qgb_variable (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	xblock_id VARCHAR(255) NOT NULL,
	name VARCHAR(32) NOT NULL,
	type VARCHAR(32) NOT NULL,
	min_value INT(6) NOT NULL,
	max_value INT(6) NOT NULL,
	decimal_places INT(3),
	FOREIGN KEY (xblock_id) REFERENCES edxapp.qgb_question_template(xblock_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci AUTO_INCREMENT=40;
