import json

hypocenter = [{'code': '011', 'name': '北海道地方'}, {'code': '012', 'name': '東北地方'}, {'code': '013', 'name': '北陸地方'}, {'code': '014', 'name': '関東甲信地方'}, {'code': '015', 'name': '小笠原地方'}, {'code': '016', 'name': '東海地方'}, {'code': '017', 'name': '近畿地方'}, {'code': '018', 'name': '中国地方'}, {'code': '019', 'name': '四国地方'}, {'code': '020', 'name': '九州地方'}, {'code': '021', 'name': '沖縄地方'}, {'code': '100', 'name': '石狩地方北部'}, {'code': '101', 'name': '石狩地方中部'}, {'code': '102', 'name': '石狩地方南部'}, {'code': '105', 'name': '渡島地方北部'}, {'code': '106', 'name': '渡島地方東部'}, {'code': '107', 'name': '渡島地方西部'}, {'code': '110', 'name': '檜山地方'}, {'code': '115', 'name': '後志地方北部'}, {'code': '116', 'name': '後志地方東部'}, {'code': '117', 'name': '後志地方西部'}, {'code': '120', 'name': '空知地方北部'}, {'code': '121', 'name': '空知地方中部'}, {'code': '122', 'name': '空知地方南部'}, {'code': '125', 'name': '上川地方北部'}, {'code': '126', 'name': '上川地方中部'}, {'code': '127', 'name': '上川地方南部'}, {'code': '130', 'name': '留萌地方中北部'}, {'code': '131', 'name': '留萌地方南部'}, {'code': '135', 'name': '宗谷地方北部'}, {'code': '136', 'name': '宗谷地方南部'}, {'code': '140', 'name': '網走地方'}, {'code': '141', 'name': '北見地方'}, {'code': '142', 'name': '紋別地方'}, {'code': '145', 'name': '胆振地方西部'}, {'code': '146', 'name': '胆振地方中東部'}, {'code': '150', 'name': '日高地方西部'}, {'code': '151', 'name': '日高地方中部'}, {'code': '152', 'name': '日高地方東部'}, {'code': '155', 'name': '十勝地方北部'}, {'code': '156', 'name': '十勝地方中部'}, {'code': '157', 'name': '十勝地方南部'}, {'code': '160', 'name': '釧路地方北部'}, {'code': '161', 'name': '釧路地方中南部'}, {'code': '165', 'name': '根室地方北部'}, {'code': '166', 'name': '根室地方中部'}, {'code': '167', 'name': '根室地方南部'}, {'code': '180', 'name': '北海道南西沖'}, {'code': '181', 'name': '北海道西方沖'}, {'code': '182', 'name': '石狩湾'}, {'code': '183', 'name': '北海道北西沖'}, {'code': '184', 'name': '宗谷海峡'}, {'code': '186', 'name': '国後島付近'}, {'code': '187', 'name': '択捉島付近'}, {'code': '188', 'name': '北海道東方沖'}, {'code': '189', 'name': '根室半島南東沖'}, {'code': '190', 'name': '釧路沖'}, {'code': '191', 'name': '十勝沖'}, {'code': '192', 'name': '浦河沖'}, {'code': '193', 'name': '苫小牧沖'}, {'code': '194', 'name': '内浦湾'}, {'code': '195', 'name': '宗谷東方沖'}, {'code': '196', 'name': '網走沖'}, {'code': '197', 'name': '択捉島南東沖'}, {'code': '200', 'name': '青森県津軽北部'}, {'code': '201', 'name': '青森県津軽南部'}, {'code': '202', 'name': '青森県三八上北地方'}, {'code': '203', 'name': '青森県下北地方'}, {'code': '210', 'name': '岩手県沿岸北部'}, {'code': '211', 'name': '岩手県沿岸南部'}, {'code': '212', 'name': '岩手県内陸北部'}, {'code': '213', 'name': '岩手県内陸南部'}, {'code': '220', 'name': '宮城県北部'}, {'code': '221', 'name': '宮城県南部'}, {'code': '222', 'name': '宮城県中部'}, {'code': '230', 'name': '秋田県沿岸北部'}, {'code': '231', 'name': '秋田県沿岸南部'}, {'code': '232', 'name': '秋田県内陸北部'}, {'code': '233', 'name': '秋田県内陸南部'}, {'code': '240', 'name': '山形県庄内地方'}, {'code': '241', 'name': '山形県最上地方'}, {'code': '242', 'name': '山形県村山地方'}, {'code': '243', 'name': '山形県置賜地方'}, {'code': '250', 'name': '福島県中通り'}, {'code': '251', 'name': '福島県浜通り'}, {'code': '252', 'name': '福島県会津'}, {'code': '280', 'name': '津軽海峡'}, {'code': '281', 'name': '山形県沖'}, {'code': '282', 'name': '秋田県沖'}, {'code': '283', 'name': '青森県西方沖'}, {'code': '284', 'name': '陸奥湾'}, {'code': '285', 'name': '青森県東方沖'}, {'code': '286', 'name': '岩手県沖'}, {'code': '287', 'name': '宮城県沖'}, {'code': '288', 'name': '三陸沖'}, {'code': '289', 'name': '福島県沖'}, {'code': '300', 'name': '茨城県北部'}, {'code': '301', 'name': '茨城県南部'}, {'code': '309', 'name': '千葉県南東沖'}, {'code': '310', 'name': '栃木県北部'}, {'code': '311', 'name': '栃木県南部'}, {'code': '320', 'name': '群馬県北部'}, {'code': '321', 'name': '群馬県南部'}, {'code': '330', 'name': '埼玉県北部'}, {'code': '331', 'name': '埼玉県南部'}, {'code': '332', 'name': '埼玉県秩父地方'}, {'code': '340', 'name': '千葉県北東部'}, {'code': '341', 'name': '千葉県北西部'}, {'code': '342', 'name': '千葉県南部'}, {'code': '349', 'name': '房総半島南方沖'}, {'code': '350', 'name': '東京都２３区'}, {'code': '351', 'name': '東京都多摩東部'}, {'code': '352', 'name': '東京都多摩西部'}, {'code': '360', 'name': '神奈川県東部'}, {'code': '361', 'name': '神奈川県西部'}, {'code': '370', 'name': '新潟県上越地方'}, {'code': '371', 'name': '新潟県中越地方'}, {'code': '372', 'name': '新潟県下越地方'}, {'code': '378', 'name': '新潟県下越沖'}, {'code': '379', 'name': '新潟県上中越沖'}, {'code': '380', 'name': '富山県東部'}, {'code': '381', 'name': '富山県西部'}, {'code': '390', 'name': '石川県能登地方'}, {'code': '391', 'name': '石川県加賀地方'}, {'code': '400', 'name': '福井県嶺北'}, {'code': '401', 'name': '福井県嶺南'}, {'code': '411', 'name': '山梨県中・西部'}, {'code': '412', 'name': '山梨県東部・富士五湖'}, {'code': '420', 'name': '長野県北部'}, {'code': '421', 'name': '長野県中部'}, {'code': '422', 'name': '長野県南部'}, {'code': '430', 'name': '岐阜県飛騨地方'}, {'code': '431', 'name': '岐阜県美濃東部'}, {'code': '432', 'name': '岐阜県美濃中西部'}, {'code': '440', 'name': '静岡県伊豆地方'}, {'code': '441', 'name': '静岡県東部'}, {'code': '442', 'name': '静岡県中部'}, {'code': '443', 'name': '静岡県西部'}, {'code': '450', 'name': '愛知県東部'}, {'code': '451', 'name': '愛知県西部'}, {'code': '460', 'name': '三重県北部'}, {'code': '461', 'name': '三重県中部'}, {'code': '462', 'name': '三重県南部'}, {'code': '469', 'name': '三重県南東沖'}, {'code': '471', 'name': '茨城県沖'}, {'code': '472', 'name': '関東東方沖'}, {'code': '473', 'name': '千葉県東方沖'}, {'code': '475', 'name': '八丈島東方沖'}, {'code': '476', 'name': '八丈島近海'}, {'code': '477', 'name': '東京湾'}, {'code': '478', 'name': '相模湾'}, {'code': '480', 'name': '伊豆大島近海'}, {'code': '481', 'name': '伊豆半島東方沖'}, {'code': '482', 'name': '三宅島近海'}, {'code': '483', 'name': '新島・神津島近海'}, {'code': '485', 'name': '駿河湾'}, {'code': '486', 'name': '駿河湾南方沖'}, {'code': '487', 'name': '遠州灘'}, {'code': '489', 'name': '三河湾'}, {'code': '490', 'name': '伊勢湾'}, {'code': '492', 'name': '若狭湾'}, {'code': '493', 'name': '福井県沖'}, {'code': '494', 'name': '石川県西方沖'}, {'code': '495', 'name': '能登半島沖'}, {'code': '497', 'name': '富山湾'}, {'code': '498', 'name': '佐渡付近'}, {'code': '499', 'name': '東海道南方沖'}, {'code': '500', 'name': '滋賀県北部'}, {'code': '501', 'name': '滋賀県南部'}, {'code': '510', 'name': '京都府北部'}, {'code': '511', 'name': '京都府南部'}, {'code': '520', 'name': '大阪府北部'}, {'code': '521', 'name': '大阪府南部'}, {'code': '530', 'name': '兵庫県北部'}, {'code': '531', 'name': '兵庫県南東部'}, {'code': '532', 'name': '兵庫県南西部'}, {'code': '540', 'name': '奈良県'}, {'code': '550', 'name': '和歌山県北部'}, {'code': '551', 'name': '和歌山県南部'}, {'code': '560', 'name': '鳥取県東部'}, {'code': '562', 'name': '鳥取県中部'}, {'code': '563', 'name': '鳥取県西部'}, {'code': '570', 'name': '島根県東部'}, {'code': '571', 'name': '島根県西部'}, {'code': '580', 'name': '岡山県北部'}, {'code': '581', 'name': '岡山県南部'}, {'code': '590', 'name': '広島県北部'}, {'code': '591', 'name': '広島県南東部'}, {'code': '592', 'name': '広島県南西部'}, {'code': '600', 'name': '徳島県北部'}, {'code': '601', 'name': '徳島県南部'}, {'code': '610', 'name': '香川県東部'}, {'code': '611', 'name': '香川県西部'}, {'code': '620', 'name': '愛媛県東予'}, {'code': '621', 'name': '愛媛県中予'}, {'code': '622', 'name': '愛媛県南予'}, {'code': '630', 'name': '高知県東部'}, {'code': '631', 'name': '高知県中部'}, {'code': '632', 'name': '高知県西部'}, {'code': '673', 'name': '土佐湾'}, {'code': '674', 'name': '紀伊水道'}, {'code': '675', 'name': '大阪湾'}, {'code': '676', 'name': '播磨灘'}, {'code': '677', 'name': '瀬戸内海中部'}, {'code': '678', 'name': '安芸灘'}, {'code': '679', 'name': '周防灘'}, {'code': '680', 'name': '伊予灘'}, {'code': '681', 'name': '豊後水道'}, {'code': '682', 'name': '山口県北西沖'}, {'code': '683', 'name': '島根県沖'}, {'code': '684', 'name': '鳥取県沖'}, {'code': '685', 'name': '隠岐島近海'}, {'code': '686', 'name': '兵庫県北方沖'}, {'code': '687', 'name': '京都府沖'}, {'code': '688', 'name': '淡路島付近'}, {'code': '689', 'name': '和歌山県南方沖'}, {'code': '700', 'name': '山口県北部'}, {'code': '702', 'name': '山口県西部'}, {'code': '703', 'name': '山口県東部'}, {'code': '704', 'name': '山口県中部'}, {'code': '710', 'name': '福岡県福岡地方'}, {'code': '711', 'name': '福岡県北九州地方'}, {'code': '712', 'name': '福岡県筑豊地方'}, {'code': '713', 'name': '福岡県筑後地方'}, {'code': '720', 'name': '佐賀県北部'}, {'code': '721', 'name': '佐賀県南部'}, {'code': '730', 'name': '長崎県北部'}, {'code': '731', 'name': '長崎県南西部'}, {'code': '732', 'name': '長崎県島原半島'}, {'code': '740', 'name': '熊本県阿蘇地方'}, {'code': '741', 'name': '熊本県熊本地方'}, {'code': '742', 'name': '熊本県球磨地方'}, {'code': '743', 'name': '熊本県天草・芦北地方'}, {'code': '750', 'name': '大分県北部'}, {'code': '751', 'name': '大分県中部'}, {'code': '752', 'name': '大分県南部'}, {'code': '753', 'name': '大分県西部'}, {'code': '760', 'name': '宮崎県北部平野部'}, {'code': '761', 'name': '宮崎県北部山沿い'}, {'code': '762', 'name': '宮崎県南部平野部'}, {'code': '763', 'name': '宮崎県南部山沿い'}, {'code': '770', 'name': '鹿児島県薩摩地方'}, {'code': '771', 'name': '鹿児島県大隅地方'}, {'code': '783', 'name': '五島列島近海'}, {'code': '784', 'name': '天草灘'}, {'code': '785', 'name': '有明海'}, {'code': '786', 'name': '橘湾'}, {'code': '787', 'name': '鹿児島湾'}, {'code': '790', 'name': '種子島近海'}, {'code': '791', 'name': '日向灘'}, {'code': '793', 'name': '奄美大島近海'}, {'code': '795', 'name': '壱岐・対馬近海'}, {'code': '796', 'name': '福岡県北西沖'}, {'code': '797', 'name': '薩摩半島西方沖'}, {'code': '798', 'name': 'トカラ列島近海'}, {'code': '799', 'name': '奄美大島北西沖'}, {'code': '820', 'name': '大隅半島東方沖'}, {'code': '821', 'name': '九州地方南東沖'}, {'code': '822', 'name': '種子島南東沖'}, {'code': '823', 'name': '奄美大島北東沖'}, {'code': '850', 'name': '沖縄本島近海'}, {'code': '851', 'name': '南大東島近海'}, {'code': '852', 'name': '沖縄本島南方沖'}, {'code': '853', 'name': '宮古島近海'}, {'code': '854', 'name': '石垣島近海'}, {'code': '855', 'name': '石垣島南方沖'}, {'code': '856', 'name': '西表島付近'}, {'code': '857', 'name': '与那国島近海'}, {'code': '858', 'name': '沖縄本島北西沖'}, {'code': '859', 'name': '宮古島北西沖'}, {'code': '860', 'name': '石垣島北西沖'}, {'code': '900', 'name': '台湾付近'}, {'code': '901', 'name': '東シナ海'}, {'code': '902', 'name': '四国沖'}, {'code': '903', 'name': '鳥島近海'}, {'code': '904', 'name': '鳥島東方沖'}, {'code': '905', 'name': 'オホーツク海南部'}, {'code': '906', 'name': 'サハリン西方沖'}, {'code': '907', 'name': '日本海北部'}, {'code': '908', 'name': '日本海中部'}, {'code': '909', 'name': '日本海西部'}, {'code': '911', 'name': '父島近海'}, {'code': '912', 'name': '千島列島'}, {'code': '913', 'name': '千島列島南東沖'}, {'code': '914', 'name': '北海道南東沖'}, {'code': '915', 'name': '東北地方東方沖'}, {'code': '916', 'name': '小笠原諸島西方沖'}, {'code': '917', 'name': '硫黄島近海'}, {'code': '918', 'name': '小笠原諸島東方沖'}, {'code': '919', 'name': '南海道南方沖'}, {'code': '920', 'name': '薩南諸島東方沖'}, {'code': '921', 'name': '本州南方沖'}, {'code': '922', 'name': 'サハリン南部付近'}, {'code': '930', 'name': '北西太平洋'}, {'code': '932', 'name': 'マリアナ諸島'}, {'code': '933', 'name': '黄海'}, {'code': '934', 'name': '朝鮮半島南部'}, {'code': '935', 'name': '朝鮮半島北部'}, {'code': '936', 'name': '中国東北部'}, {'code': '937', 'name': 'ウラジオストク付近'}, {'code': '938', 'name': 'シベリア南部'}, {'code': '939', 'name': 'サハリン近海'}, {'code': '940', 'name': 'アリューシャン列島'}, {'code': '941', 'name': 'カムチャツカ半島付近'}, {'code': '942', 'name': '北米西部'}, {'code': '943', 'name': '北米中部'}, {'code': '944', 'name': '北米東部'}, {'code': '945', 'name': '中米'}, {'code': '946', 'name': '南米西部'}, {'code': '947', 'name': '南米中部'}, {'code': '948', 'name': '南米東部'}, {'code': '949', 'name': '北東太平洋'}, {'code': '950', 'name': '南太平洋'}, {'code': '951', 'name': 'インドシナ半島付近'}, {'code': '952', 'name': 'フィリピン付近'}, {'code': '953', 'name': 'インドネシア付近'}, {'code': '954', 'name': 'グアム付近'}, {'code': '955', 'name': 'ニューギニア付近'}, {'code': '956', 'name': 'ニュージーランド付近'}, {'code': '957', 'name': 'オーストラリア付近'}, {'code': '958', 'name': 'シベリア付近'}, {'code': '959', 'name': 'ロシア西部'}, {'code': '960', 'name': 'ロシア中部'}, {'code': '961', 'name': 'ロシア東部'}, {'code': '962', 'name': '中央アジア'}, {'code': '963', 'name': '中国西部'}, {'code': '964', 'name': '中国中部'}, {'code': '965', 'name': '中国東部'}, {'code': '966', 'name': 'インド付近'}, {'code': '967', 'name': 'インド洋'}, {'code': '968', 'name': '中東'}, {'code': '969', 'name': 'ヨーロッパ西部'}, {'code': '970', 'name': 'ヨーロッパ中部'}, {'code': '971', 'name': 'ヨーロッパ東部'}, {'code': '972', 'name': '地中海'}, {'code': '973', 'name': 'アフリカ西部'}, {'code': '974', 'name': 'アフリカ中部'}, {'code': '975', 'name': 'アフリカ東部'}, {'code': '976', 'name': '北大西洋'}, {'code': '977', 'name': '南大西洋'}, {'code': '978', 'name': '北極付近'}, {'code': '979', 'name': '南極付近'}, {'code': '999', 'name': '遠地'}]
saibun = [{'code': '100', 'name': '石狩地方北部'}, {'code': '101', 'name': '石狩地方中部'}, {'code': '102', 'name': '石狩地方南部'}, {'code': '105', 'name': '渡島地方北部'}, {'code': '106', 'name': '渡島地方東部'}, {'code': '107', 'name': '渡島地方西部'}, {'code': '110', 'name': '檜山地方'}, {'code': '115', 'name': '後志地方北部'}, {'code': '116', 'name': '後志地方東部'}, {'code': '117', 'name': '後志地方西部'}, {'code': '119', 'name': '北海道奥尻島'}, {'code': '120', 'name': '空知地方北部'}, {'code': '121', 'name': '空知地方中部'}, {'code': '122', 'name': '空知地方南部'}, {'code': '125', 'name': '上川地方北部'}, {'code': '126', 'name': '上川地方中部'}, {'code': '127', 'name': '上川地方南部'}, {'code': '130', 'name': '留萌地方中北部'}, {'code': '131', 'name': '留萌地方南部'}, {'code': '135', 'name': '宗谷地方北部'}, {'code': '136', 'name': '宗谷地方南部'}, {'code': '139', 'name': '北海道利尻礼文'}, {'code': '140', 'name': '網走地方'}, {'code': '141', 'name': '北見地方'}, {'code': '142', 'name': '紋別地方'}, {'code': '145', 'name': '胆振地方西部'}, {'code': '146', 'name': '胆振地方中東部'}, {'code': '150', 'name': '日高地方西部'}, {'code': '151', 'name': '日高地方中部'}, {'code': '152', 'name': '日高地方東部'}, {'code': '155', 'name': '十勝地方北部'}, {'code': '156', 'name': '十勝地方中部'}, {'code': '157', 'name': '十勝地方南部'}, {'code': '160', 'name': '釧路地方北部'}, {'code': '161', 'name': '釧路地方中南'}, {'code': '165', 'name': '根室地方北部'}, {'code': '166', 'name': '根室地方中部'}, {'code': '167', 'name': '根室地方南部'}, {'code': '200', 'name': '青森県津軽北部'}, {'code': '201', 'name': '青森県津軽南部'}, {'code': '202', 'name': '青森県三八上北'}, {'code': '203', 'name': '青森県下北'}, {'code': '210', 'name': '岩手県沿岸北部'}, {'code': '211', 'name': '岩手県沿岸南部'}, {'code': '212', 'name': '岩手県内陸北部'}, {'code': '213', 'name': '岩手県内陸南部'}, {'code': '220', 'name': '宮城県北部'}, {'code': '221', 'name': '宮城県南部'}, {'code': '222', 'name': '宮城県中部'}, {'code': '230', 'name': '秋田県沿岸北部'}, {'code': '231', 'name': '秋田県沿岸南部'}, {'code': '232', 'name': '秋田県内陸北部'}, {'code': '233', 'name': '秋田県内陸南部'}, {'code': '240', 'name': '山形県庄内'}, {'code': '241', 'name': '山形県最上'}, {'code': '242', 'name': '山形県村山'}, {'code': '243', 'name': '山形県置賜'}, {'code': '250', 'name': '福島県中通り'}, {'code': '251', 'name': '福島県浜通り'}, {'code': '252', 'name': '福島県会津'}, {'code': '300', 'name': '茨城県北部'}, {'code': '301', 'name': '茨城県南部'}, {'code': '310', 'name': '栃木県北部'}, {'code': '311', 'name': '栃木県南部'}, {'code': '320', 'name': '群馬県北部'}, {'code': '321', 'name': '群馬県南部'}, {'code': '330', 'name': '埼玉県北部'}, {'code': '331', 'name': '埼玉県南部'}, {'code': '332', 'name': '埼玉県秩父'}, {'code': '340', 'name': '千葉県北東部'}, {'code': '341', 'name': '千葉県北西部'}, {'code': '342', 'name': '千葉県南部'}, {'code': '350', 'name': '東京都２３区'}, {'code': '351', 'name': '東京都多摩東部'}, {'code': '352', 'name': '東京都多摩西部'}, {'code': '354', 'name': '神津島'}, {'code': '355', 'name': '伊豆大島'}, {'code': '356', 'name': '新島'}, {'code': '357', 'name': '三宅島'}, {'code': '358', 'name': '八丈島'}, {'code': '359', 'name': '小笠原'}, {'code': '360', 'name': '神奈川県東部'}, {'code': '361', 'name': '神奈川県西部'}, {'code': '370', 'name': '新潟県上越'}, {'code': '371', 'name': '新潟県中越'}, {'code': '372', 'name': '新潟県下越'}, {'code': '375', 'name': '新潟県佐渡'}, {'code': '380', 'name': '富山県東部'}, {'code': '381', 'name': '富山県西部'}, {'code': '390', 'name': '石川県能登'}, {'code': '391', 'name': '石川県加賀'}, {'code': '400', 'name': '福井県嶺北'}, {'code': '401', 'name': '福井県嶺南'}, {'code': '411', 'name': '山梨県中・西部'}, {'code': '412', 'name': '山梨県東部・富士五湖'}, {'code': '420', 'name': '長野県北部'}, {'code': '421', 'name': '長野県中部'}, {'code': '422', 'name': '長野県南部'}, {'code': '430', 'name': '岐阜県飛騨'}, {'code': '431', 'name': '岐阜県美濃東部'}, {'code': '432', 'name': '岐阜県美濃中西部'}, {'code': '440', 'name': '静岡県伊豆'}, {'code': '441', 'name': '静岡県東部'}, {'code': '442', 'name': '静岡県中部'}, {'code': '443', 'name': '静岡県西部'}, {'code': '450', 'name': '愛知県東部'}, {'code': '451', 'name': '愛知県西部'}, {'code': '460', 'name': '三重県北部'}, {'code': '461', 'name': '三重県中部'}, {'code': '462', 'name': '三重県南部'}, {'code': '500', 'name': '滋賀県北部'}, {'code': '501', 'name': '滋賀県南部'}, {'code': '510', 'name': '京都府北部'}, {'code': '511', 'name': '京都府南部'}, {'code': '520', 'name': '大阪府北部'}, {'code': '521', 'name': '大阪府南部'}, {'code': '530', 'name': '兵庫県北部'}, {'code': '531', 'name': '兵庫県南東部'}, {'code': '532', 'name': '兵庫県南西部'}, {'code': '535', 'name': '兵庫県淡路島'}, {'code': '540', 'name': '奈良県'}, {'code': '550', 'name': '和歌山県北部'}, {'code': '551', 'name': '和歌山県南部'}, {'code': '560', 'name': '鳥取県東部'}, {'code': '562', 'name': '鳥取県中部'}, {'code': '563', 'name': '鳥取県西部'}, {'code': '570', 'name': '島根県東部'}, {'code': '571', 'name': '島根県西部'}, {'code': '575', 'name': '島根県隠岐'}, {'code': '580', 'name': '岡山県北部'}, {'code': '581', 'name': '岡山県南部'}, {'code': '590', 'name': '広島県北部'}, {'code': '591', 'name': '広島県南東部'}, {'code': '592', 'name': '広島県南西部'}, {'code': '600', 'name': '徳島県北部'}, {'code': '601', 'name': '徳島県南部'}, {'code': '610', 'name': '香川県東部'}, {'code': '611', 'name': '香川県西部'}, {'code': '620', 'name': '愛媛県東予'}, {'code': '621', 'name': '愛媛県中予'}, {'code': '622', 'name': '愛媛県南予'}, {'code': '630', 'name': '高知県東部'}, {'code': '631', 'name': '高知県中部'}, {'code': '632', 'name': '高知県西部'}, {'code': '700', 'name': '山口県北部'}, {'code': '702', 'name': '山口県西部'}, {'code': '703', 'name': '山口県東部'}, {'code': '704', 'name': '山口県中部'}, {'code': '710', 'name': '福岡県福岡'}, {'code': '711', 'name': '福岡県北九州'}, {'code': '712', 'name': '福岡県筑豊'}, {'code': '713', 'name': '福岡県筑後'}, {'code': '720', 'name': '佐賀県北部'}, {'code': '721', 'name': '佐賀県南部'}, {'code': '730', 'name': '長崎県北部'}, {'code': '731', 'name': '長崎県南西部'}, {'code': '732', 'name': '長崎県島原半島'}, {'code': '735', 'name': '長崎県対馬'}, {'code': '736', 'name': '長崎県壱岐'}, {'code': '737', 'name': '長崎県五島'}, {'code': '740', 'name': '熊本県阿蘇'}, {'code': '741', 'name': '熊本県熊本'}, {'code': '742', 'name': '熊本県球磨'}, {'code': '743', 'name': '熊本県天草・芦北'}, {'code': '750', 'name': '大分県北部'}, {'code': '751', 'name': '大分県中部'}, {'code': '752', 'name': '大分県南部'}, {'code': '753', 'name': '大分県西部'}, {'code': '760', 'name': '宮崎県北部平野部'}, {'code': '761', 'name': '宮崎県北部山沿い'}, {'code': '762', 'name': '宮崎県南部平野部'}, {'code': '763', 'name': '宮崎県南部山沿い'}, {'code': '770', 'name': '鹿児島県薩摩'}, {'code': '771', 'name': '鹿児島県大隅'}, {'code': '774', 'name': '鹿児島県十島村'}, {'code': '775', 'name': '鹿児島県甑島'}, {'code': '776', 'name': '鹿児島県種子島'}, {'code': '777', 'name': '鹿児島県屋久島'}, {'code': '778', 'name': '鹿児島県奄美北部'}, {'code': '779', 'name': '鹿児島県奄美南部'}, {'code': '800', 'name': '沖縄県本島北部'}, {'code': '801', 'name': '沖縄県本島中南部'}, {'code': '802', 'name': '沖縄県久米島'}, {'code': '803', 'name': '沖縄県大東島'}, {'code': '804', 'name': '沖縄県宮古島'}, {'code': '805', 'name': '沖縄県石垣島'}, {'code': '806', 'name': '沖縄県与那国島'}, {'code': '807', 'name': '沖縄県西表島'}]

def parse_data(data):
    global saibun
    global hypocenter
    json_dict = {}
    json_dict["issue"] = {}
    json_dict["earthquake"] = {}
    json_dict["earthquake"]["hypocenter"] = {}
    json_dict["accuracy"] = {}
    json_dict["area"] = []
    # ヘッダー部分
    ## 電文種別
    title = data[0:2]
    match title:
        case "35":
            json_dict["title"] = "最大予測震度のみの緊急地震速報"
        case "36":
            json_dict["title"] = "Ｍ、最大予測震度及び主要動到達予測時刻の緊急地震速報"
        case "37":
            json_dict["title"] = "Ｍ、最大予測震度及び主要動到達時刻の緊急地震速報"
        case "38":
            json_dict["title"] = "テスト電文"
        case "39":
            json_dict["title"] = "キャンセル（取り消し）情報"
        case "47":
            json_dict["title"] = "般向け緊急地震速報"
        case "48":
            json_dict["title"] = "キャンセル報"
        case "61":
            json_dict["title"] = "リアルタイム震度電文（工学的基盤面の値）、リアルタイム震度電文のキャンセル報"
    ## 発信官署
    source = data[3:5]
    json_dict["issue"]["source"] = {}
    match source:
        case "01":
            json_dict["issue"]["source"] = "札幌"
        case "02":
            json_dict["issue"]["source"] = "仙台"
        case "03":
            json_dict["issue"]["source"] = "気象庁本庁"
        case "04":
            json_dict["issue"]["source"] = "大阪管区気象台"
        case "05":
            json_dict["issue"]["source"] = "福岡"
    ## 電文の種類
    telegram_type = data[6:8]
    json_dict["issue"]["telegram_type"] = {}
    match telegram_type:
        case "00":
            json_dict["issue"]["telegram_type"] = "通常"
        case "01":
            json_dict["issue"]["telegram_type"] = "訓練"
        case "10":
            json_dict["issue"]["telegram_type"] = "通常の取り消し"
        case "11":
            json_dict["issue"]["telegram_type"] = "訓練の取り消し"
        case "20":
            json_dict["issue"]["telegram_type"] = "参考情報またはテスト電文"
        case "30":
            json_dict["issue"]["telegram_type"] = "コード部全体の配信試験"
    ## 電文発信時刻
    outgoing_time_moto = data[9:21]
    outgoing_time = "20" + outgoing_time_moto[0:2] + "-" + outgoing_time_moto[2:4] + "-" + outgoing_time_moto[4:6]
    outgoing_time = outgoing_time + " " + outgoing_time_moto[6:8] + ":" + outgoing_time_moto[8:10] + ":" + outgoing_time_moto[10:12]
    json_dict["issue"]["outgoing_time"] = outgoing_time
    # 電文の内容
    body = data[26:]
    ## 発生時刻(PLUMの場合は検知時刻)
    occurrence_time_moto = body[0:12]
    occurrence_time = "20" + occurrence_time_moto[0:2] + "-" + occurrence_time_moto[2:4] + "-" + occurrence_time_moto[4:6]
    occurrence_time = occurrence_time + " " + occurrence_time_moto[6:8] + ":" + occurrence_time_moto[8:10] + ":" + occurrence_time_moto[10:12]
    json_dict["earthquake"]["occurrence_time"] = occurrence_time
    ## EventId
    eventid = body[15:29]
    json_dict["issue"]["EventID"] = eventid
    ## ステータス(最終報とほぼ同じ)
    status = body[33]
    json_dict["issue"]["status"] = {}
    match status:
        case "0":
            json_dict["issue"]["status"] = "通常発表時"
        case "9":
            json_dict["issue"]["status"] = "最終の緊急地震速報（予報）"
        case _:
            json_dict["issue"]["status"] = "未設定時"
    ## 警報発表中か
    match body[96]:
        case "0":
            json_dict["issue"]["isWarning"] = False
        case "1":
            json_dict["issue"]["isWarning"] = True
        case _:
            json_dict["issue"]["isWarning"] = False
    ## 最終報か
    isFinal = status
    match isFinal:
        case "9":
            json_dict["issue"]["isFinal"] = True
        case _:
            json_dict["issue"]["isFinal"] = False
    ## 予測手法(PLUMか)
    isPLUM = body[97]
    if isPLUM == "9":
        json_dict["issue"]["isPLUM"] = True
    else:
        json_dict["issue"]["isPLUM"] = False
    ## 震央コード
    hypocenter_code = body[60:63]
    if hypocenter_code == "///":
        json_dict["earthquake"]["hypocenter"]["code"] = "不明"
        json_dict["earthquake"]["hypocenter"]["name"] = "不明"
        json_dict["issue"]["isCancelled"] = True
    else:
        json_dict["earthquake"]["hypocenter"]["code"] = hypocenter_code
        hypo_name = next((item for item in hypocenter if item['code'] == hypocenter_code), None)
        json_dict["earthquake"]["hypocenter"]["name"] = hypo_name["name"]
        json_dict["issue"]["isCancelled"] = False
    ## n報(99以上は非対応)
    serial = body[34:36]
    json_dict["issue"]["Serial"] = serial
    ## 震源の経緯度(南緯・西経の場合は-になる)
    hypocenter_lat = body[64:68]
    hypocenter_lon = body[69:74]
    match hypocenter_lat[0]:
        case "N":
            json_dict["earthquake"]["hypocenter"]["lat"] = str(float(hypocenter_lat[1:]) / 10)
        case "S":
            json_dict["earthquake"]["hypocenter"]["lat"] = str(-float(hypocenter_lat[1:]) / 10)
        case _:
            json_dict["earthquake"]["hypocenter"]["lat"] = "不明"
    match hypocenter_lon[0]:
        case "E":
            json_dict["earthquake"]["hypocenter"]["lon"] = str(float(hypocenter_lon[1:]) / 10)
        case "W":
            json_dict["earthquake"]["hypocenter"]["lon"] = str(-float(hypocenter_lon[1:]) / 10)
        case _:
            json_dict["earthquake"]["hypocenter"]["lon"] = "不明"
    ## 深さ(仮定震源要素の場合は10固定)
    if body[75:78] == "///":
        depth = "不明"
    else:
        depth = str(int(body[75:78]) * 1)
    json_dict["earthquake"]["hypocenter"]["depth"] = depth
    ## マグニチュード(仮定震源要素の場合は1.0固定)
    if body[79:81] == "//":
        magnitude = "不明"
    else:
        magnitude = str(float(body[79:81]) / 10)
    json_dict["earthquake"]["hypocenter"]["magnitude"] = magnitude
    ## 震度(文字型 5+,5-など)
    maxScale = body[82:84]
    json_dict["earthquake"]["maxScale"] = shindo_henkan(maxScale)
    ## データの精度
    accuracy = body[87:91]
    hyp_accuracy = accuracy[0]
    dep_accuracy = accuracy[1]
    mag_accuracy = accuracy[2]
    mag_station = accuracy[3]
    ### 震央精度
    json_dict["accuracy"]["hypocenter"] = {}
    match hyp_accuracy:
        case "1":
            json_dict["accuracy"]["hypocenter"] = "P 波／S 波レベル越え、IPF 法（1 点）、または仮定震源要素"
        case "2":
            json_dict["accuracy"]["hypocenter"] = "IPF 法（2 点）"
        case "3":
            json_dict["accuracy"]["hypocenter"] = "IPF 法（3 点／4 点）"
        case "4":
            json_dict["accuracy"]["hypocenter"] = "IPF 法（5 点以上）"
        case "5":
            json_dict["accuracy"]["hypocenter"] = "防災科研システム（4 点以下、または精度情報なし）"
        case "6":
            json_dict["accuracy"]["hypocenter"] = "防災科研システム（5 点以上）"
        case "7":
            json_dict["accuracy"]["hypocenter"] = "EPOS（海域〔観測網外〕）"
        case "8":
            json_dict["accuracy"]["hypocenter"] = "EPOS（内陸〔観測網内〕）"
        case "9":
            json_dict["accuracy"]["hypocenter"] = "予備"
        case _:
            json_dict["accuracy"]["hypocenter"] = "不明、未設定時、キャンセル時"
    ### 深さ精度
    json_dict["accuracy"]["depth"] = {}
    match dep_accuracy:
        case "1":
            json_dict["accuracy"]["depth"] = "P 波／S 波レベル越え、IPF 法（1 点）、または仮定震源要素"
        case "2":
            json_dict["accuracy"]["depth"] = "IPF 法（2 点）"
        case "3":
            json_dict["accuracy"]["depth"] = "IPF 法（3 点／4 点）"
        case "4":
            json_dict["accuracy"]["depth"] = "IPF 法（5 点以上）"
        case "5":
            json_dict["accuracy"]["depth"] = "防災科研システム（4 点以下、または精度情報なし）"
        case "6":
            json_dict["accuracy"]["depth"] = "防災科研システム（5 点以上）"
        case "7":
            json_dict["accuracy"]["depth"] = "EPOS（海域〔観測網外〕）"
        case "8":
            json_dict["accuracy"]["depth"] = "EPOS（内陸〔観測網内〕）"
        case "9":
            json_dict["accuracy"]["depth"] = "予備"
        case _:
            json_dict["accuracy"]["depth"] = "不明、未設定時、キャンセル時"
    ### マグニチュード精度
    json_dict["accuracy"]["magnitude"] = {}
    match mag_accuracy:
        case "1":
            json_dict["accuracy"]["magnitude"] = "未定義"
        case "2":
            json_dict["accuracy"]["magnitude"] = "防災科研システム 〔防災科研Hi-net データ〕"
        case "3":
            json_dict["accuracy"]["magnitude"] = "全点P 相"
        case "4":
            json_dict["accuracy"]["magnitude"] = "P 相／全相混在"
        case "5":
            json_dict["accuracy"]["magnitude"] = "全点全相"
        case "6":
            json_dict["accuracy"]["magnitude"] = "EPOS"
        case "7":
            json_dict["accuracy"]["magnitude"] = "未定義"
        case "8":
            json_dict["accuracy"]["magnitude"] = "P 波／S 波レベル越え、または仮定震源要素"
        case "9":
            json_dict["accuracy"]["magnitude"] = "予備"
        case _:
            json_dict["accuracy"]["magnitude"] = "不明、未設定時、キャンセル時"
    ### マグニチュード使用観測点数（※気象庁の部内システムでの利用）
    json_dict["accuracy"]["magnitude_station"] = {}
    match mag_station:
        case "1":
            json_dict["accuracy"]["magnitude_station"] = "1 点、P 波／S 波レベル越え、または仮定震源要素"
        case "2":
            json_dict["accuracy"]["magnitude_station"] = "2 点"
        case "3":
            json_dict["accuracy"]["magnitude_station"] = "3 点"
        case "4":
            json_dict["accuracy"]["magnitude_station"] = "4 点"
        case "5":
            json_dict["accuracy"]["magnitude_station"] = "5 点以上"
        case "/":
            json_dict["accuracy"]["magnitude_station"] = "不明、未設定時、キャンセル時"
        case _:
            json_dict["accuracy"]["magnitude_station"] = "未使用"
    ## 海域か陸域("land" or "sea" or "unknown")
    sea_or_land = body[95]
    match sea_or_land:
        case "0":
            json_dict["earthquake"]["sea_or_land"] = "land"
        case "1":
            json_dict["earthquake"]["sea_or_land"] = "sea"
        case _:
            json_dict["earthquake"]["sea_or_land"] = "unknown"
    ## 推定最大震度の変化
    maxScale_change = body[103]
    json_dict["earthquake"]["maxScale_change"] = {}
    match maxScale_change:
        case "0":
            json_dict["earthquake"]["maxScale_change"] = "ほとんど変化なし"
        case "1":
            json_dict["earthquake"]["maxScale_change"] = "最大予測震度が1.0 以上大きくなった。"
        case "2":
            json_dict["earthquake"]["maxScale_change"] = "最大予測震度が1.0 以上小さくなった。"
        case "/":
            json_dict["earthquake"]["maxScale_change"] = "不明、未設定時、キャンセル時"
        case _:
            json_dict["earthquake"]["maxScale_change"] = "未定義"
    ## 推定最大震度の変化理由
    maxScale_change_reason = body[104]
    json_dict["earthquake"]["maxScale_change_reason"] = {}
    match maxScale_change_reason:
        case "0":
            json_dict["earthquake"]["maxScale_change_reason"] = "変化なし"
        case "1":
            json_dict["earthquake"]["maxScale_change_reason"] = "主としてＭが変化したため(1.0 以上)。"
        case "2":
            json_dict["earthquake"]["maxScale_change_reason"] = "主として震源位置が変化したため(10.0km 以上)。"
        case "3":
            json_dict["earthquake"]["maxScale_change_reason"] = "Ｍ及び震源位置が変化したため(1 と2 の複合条件)。"
        case "4":
            json_dict["earthquake"]["maxScale_change_reason"] = "震源の深さが変化したため。"
        case "9":
            json_dict["earthquake"]["maxScale_change_reason"] = "PLUM 法による予測により変化したため。"
        case "/":
            json_dict["earthquake"]["maxScale_change_reason"] = "不明、未設定時、キャンセル時"
        case _:
            json_dict["earthquake"]["maxScale_change_reason"] = "未定義"
    # 地域ごとの予測震度
    yosoushindo = data[139:]
    yosoushindo_items = int((len(data) - 144) / 20)
    for i in range(yosoushindo_items):
        yosoushindo_temp = yosoushindo[i*20:i*20+20]
        yosoushindo_json = {}
        ## 地域コード
        yosoushindo_tiiki_code = yosoushindo_temp[0:3]
        tiiki_name = next((item for item in saibun if item['code'] == yosoushindo_tiiki_code), None)
        yosoushindo_json["code"] = yosoushindo_tiiki_code
        yosoushindo_json["name"] = tiiki_name["name"]
        ## 最大予測震度
        yosoushindo_from = yosoushindo_temp[7:9]
        yosoushindo_to = yosoushindo_temp[5:7]
        if yosoushindo_to == "//":
            yosoushindo_json["From"] = shindo_henkan(yosoushindo_to)
            yosoushindo_json["To"] = "over"
        else:
            yosoushindo_json["From"] = shindo_henkan(yosoushindo_from)
            yosoushindo_json["To"] = shindo_henkan(yosoushindo_to)
        ## 到達予想
        yosoushindo_arrival_time = yosoushindo_temp[10:16]
        if yosoushindo_arrival_time == "//////":
            yosoushindo_json["arrival_time"] = "//////"
        else:
            yosoushindo_arrival_time = yosoushindo_arrival_time[0:2] + ":" + yosoushindo_arrival_time[2:4] + ":" + yosoushindo_arrival_time[4:6]
            yosoushindo_json["arrival_time"] = yosoushindo_arrival_time
        ## 警報状況と到達予測状況
        yosoushindo_warning_and_status = yosoushindo_temp[17:19]
        yosoushindo_warning = yosoushindo_warning_and_status[0:1]
        yosoushindo_status = yosoushindo_warning_and_status[1:]
        match yosoushindo_warning:
            case "1":
                yosoushindo_json["warning"] = True
            case _:
                yosoushindo_json["warning"] = False
        yosoushindo_json["status"] = {}
        match yosoushindo_status:
            case "0":
                yosoushindo_json["status"] = "未到達"
            case "1":
                yosoushindo_json["status"] = "既に到達と予測"
            case "9":
                yosoushindo_json["status"] = "主要動到達時刻の予測なし（PLUM 法による予測）"
            case _:
                yosoushindo_json["status"] = "不明"
        ## 配列として予想震度を追加
        json_dict["area"].append(yosoushindo_json)
    json_dict["original_telegram"] = data
    # jsonを返す
    return json.dumps(json_dict, ensure_ascii=False)
 
def shindo_henkan(data):
    if data == "//":
            shindo = "不明"
    else:
        if data == "01" or data == "02" or data == "03" or data == "04" or data == "07":
            shindo = str(int(data) * 1)
        else:
            shindo = data
    return shindo