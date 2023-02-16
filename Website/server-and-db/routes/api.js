const express = require('express');
const router = express.Router();
const visitorController = require('../controllers/visitor');
const visitRecordController = require('../controllers/visitRecord');
const productController = require('../controllers/product');
const manufacturerController = require('../controllers/manufacturer');

router.get('/manufacturers', manufacturerController.all);
router.get('/manufacturers/:id', manufacturerController.byId);
router.post('/manufacturers', manufacturerController.create);
router.put('/manufacturers/:id', manufacturerController.update);
router.delete('/manufacturers/:id', manufacturerController.remove);

router.get('/products', productController.all);
router.get('/products/:id', productController.byId);
router.post('/products', productController.create);
router.put('/products/:id', productController.update);
router.delete('/products/:id', productController.remove);

router.get('/visitors', visitorController.all);
router.get('/visitors/:id', visitorController.byId);
router.post('/visitors', visitorController.create);
router.put('/visitors/:id', visitorController.update);
router.delete('/visitors/:id', visitorController.remove);

router.get('/visitRecords', visitRecordController.all);
router.get('/visitRecords/week', visitRecordController.byWeek);
router.get('/visitRecords/cnt', visitRecordController.cntRank);
router.get('/visitRecords/:id', visitRecordController.byId);
router.post('/visitRecords', visitRecordController.create);
router.put('/visitRecords/:id', visitRecordController.update);
router.delete('/visitRecords/:id', visitRecordController.remove);

module.exports = router;