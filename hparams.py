import tensorflow as tf
from text import symbols

def hparam_dict():

    hparams_dict={'epochs':500,
                   'iters_per_checkpoint':1000,
                   'seed':1234,
                   'dynamic_loss_scaling':True,
                   'fp16_run':False,
                   'distributed_run':False,
                   'dist_backend':"nccl",
                   'dist_url':"tcp://localhost:54321",
                   'cudnn_enabled':True,
                   'cudnn_benchmark':False,
                   'ignore_layers':['embedding.weight'],
                   'load_mel_from_disk':False,
                   'training_files':'filelists/ljs_audio_text_train_filelist.txt',
                   'validation_files':'filelists/ljs_audio_text_val_filelist.txt',
                   'text_cleaners':['english_cleaners'],
                   'max_wav_value':32768.0,
                   'sampling_rate':22050,
                   'filter_length':1024,
                   'hop_length':256,
                   'win_length':1024,
                   'n_mel_channels':80,
                   'mel_fmin':0.0,
                   'mel_fmax':8000.0,
                   'n_symbols':len(symbols),
                   'symbols_embedding_dim':512,
                   'encoder_kernel_size':5,
                   'encoder_n_convolutions':3,
                   'encoder_embedding_dim':512,
                   'n_frames_per_step':1,
                   'decoder_rnn_dim':1024,
                   'prenet_dim':256,
                   'max_decoder_steps':10000,
                   'gate_threshold':0.5,
                   'p_attention_dropout':0.1,
                   'p_decoder_dropout':0.1,
                   'attention_rnn_dim':1024,
                   'attention_dim':128,
                   'attention_location_n_filters':32,
                   'attention_location_kernel_size':31,
                   'postnet_embedding_dim':512,
                   'postnet_kernel_size':5,
                   'postnet_n_convolutions':5,
                   'use_saved_learning_rate':False,
                   'learning_rate':1e-3,
                   'weight_decay':1e-6,
                   'grad_clip_thresh':1.0,
                   'batch_size':64,
                   'mask_padding':True}

    return hparams_dict
