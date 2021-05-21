import { takeEvery, put } from 'redux-saga/effects';

function* workerSaga() {
    console.log('Hey from worker');
    yield put({ type: 'ACTION_FROM_WORKER' });
}

// watcher saga
function* rootSaga() {
    yield takeEvery('HELLO', workerSaga);
}

export default rootSaga;
