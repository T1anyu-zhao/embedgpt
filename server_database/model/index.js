const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const model = mongoose.model.bind(mongoose);
const ObjectId = mongoose.Schema.Types.ObjectId;

const productSchema = Schema({
  id: ObjectId,
  name: String,
  image: String,
  price: Number,
  description: String,
  manufacturer: { type: ObjectId, ref: 'Manufacturer' }
});

const manufacturerSchema = Schema({
  id: ObjectId,
  name: String,
});

const visitorSchema = Schema({
  id: ObjectId,
  name: String,
  department: String,
  image: String,
  lastVisit: String,
});

const visitRecordSchema = Schema({
  id: ObjectId,
  date: String,
  photoRecord: String,
  visitor: { type: ObjectId, ref: 'Visitor' },
});

const Product = model('Product', productSchema);
const Manufacturer = model('Manufacturer', manufacturerSchema);
const Visitor = model('Visitor', visitorSchema);
const VisitRecord = model('VisitorRecord', visitRecordSchema);


module.exports = { Product, Manufacturer, Visitor, VisitRecord };