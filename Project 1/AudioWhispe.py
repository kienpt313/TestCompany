import openai
API_key = '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'
model_id='whisper-1'
media_file_path='audio.mp3'
media_file=open(media_file_path,'rb')
respone=openai.Audio.transcribe(
	api_key=API_key,
	model=model_id,
	file=media_file,
	response_format='text'
)
with open("transcription.txt",'w') as f:
	f.write(respone)