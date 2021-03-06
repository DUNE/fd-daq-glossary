def options(opt):
    opt.load('tex')
    opt.add_option('--debug', default=False, action='store_true',
                   help="run pdfLaTeX so that it goes into interactive mode on error.")

def configure(cfg):
    cfg.load('tex')

def build(bld):
    prompt_level = 0
    if bld.options.debug:
        prompt_level = 1

    name = "daq-vocabulary"

    bld(features='tex', prompt = prompt_level,
        source = name + ".tex",
        target = name + ".pdf")

