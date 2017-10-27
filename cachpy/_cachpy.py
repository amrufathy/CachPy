from __future__ import print_function


def cachpy(filepath=None, ignore_cache=False, reload_cache=False, verbose=False):
    def _cachpy_decorator(fn):

        from functools import wraps

        @wraps(fn)
        def _fn_wrapper(*args, **kwargs):
            user_file_name = filepath
            _print = lambda x: None

            if verbose:
                _print = print

            _print('Verbose mode on')

            if ignore_cache:
                _print('Ignoring caching. Re-evaluating the function...')
                return fn(*args, **kwargs)

            from sys import modules
            from os import makedirs
            from os.path import dirname, join, exists

            file_name, file_path = None, None

            if not user_file_name:
                _print('No file name given. Using function name instead...')
                file_name = '{}__{}.pickle'.format(fn.__module__.strip('__'), fn.__name__)

                base_path = dirname(modules['__main__'].__file__)
                base_path = join(base_path, '.pickles')

                if not exists(base_path):
                    _print('Creating directory \'{}\' ...'.format(base_path))
                    makedirs(base_path)

                file_path = join(base_path, file_name)

            file_path = user_file_name if user_file_name else file_path
            isFileExist = exists(file_path)

            try:
                # For Python 2.x
                import cPickle as pickle
            except ImportError:
                # Normal pickle module
                import pickle

            if isFileExist and not reload_cache:
                _print('Returning cached result...')
                with open(file_path, 'rb') as f:
                    return pickle.load(f)
            elif isFileExist and reload_cache:
                _print('Reloading cached result. Evaluating...')
            else:
                _print('Result not cached. Evaluating...')

            result = fn(*args, **kwargs)
            _print('Writing new result to \'{}\''.format(file_path))
            with open(file_path, 'wb') as f:
                pickle.dump(obj=result, file=f, protocol=pickle.HIGHEST_PROTOCOL)

            return result

        return _fn_wrapper

    return _cachpy_decorator
