ブログ連動企画

機械学習関連の各種デモ

動作確認環境

　１．Windows10に「anaconda」をインストール

�２．仮想環境：conda create -n XXXXXXX python=3.7
　　　例　conda create -n demos python=3.7

　３．仮想環境をアクティブ：activate XXXXXXX
　    
　４．動作に必要なライブラリインストール
　
		pip install --upgrade tensorflow
		pip install django
		pip install django-bootstrap4
		pip install django-widget-tweaks
		pip install "tensorflow_hub==0.4.0"
		pip install Pillow
		pip install gensim
	
	 
