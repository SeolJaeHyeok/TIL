import { takeEvery } from 'redux-saga/effects';
import { IMAGES } from '../constants';

function* handleImagesLoad() {
    console.log('fetching images from unsplash');
}

// watcher saga
function* rootSaga() {
    yield takeEvery(IMAGES.LOAD, handleImagesLoad);
}

export default rootSaga;
