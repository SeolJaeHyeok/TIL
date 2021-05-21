import { takeEvery, select, call, put } from 'redux-saga/effects';

import { IMAGES } from '../constants';
import { fetchImages } from '../api';
import { setImages, setError } from '../actions';

const getPage = (state) => state.nextPage;

function* handleImagesLoad() {
    try {
        const page = yield select(getPage);
        const images = yield call(fetchImages, page);
        yield put(setImages(images));
    } catch (error) {
        // dispatch error
        yield put(setError(error.toString()));
    }
}

// watcher saga
export default function* watchImagesLoad() {
    yield takeEvery(IMAGES.LOAD, handleImagesLoad);
}
