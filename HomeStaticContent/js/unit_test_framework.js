const assert = require('assert')
require('analytics.js')
require('mylogin.js')
require('realtimetracker.js')
require('webrtc-patch.js')


describe('analytics', function() {
  // describes a module with nested "describe" functions
  describe('test-name', function() {
it('should return true', () => {
  assert.equal(add("test-name"), "test-name")
 })

it('should return true', () => {
  assert.equal(add(""), "")
})

it('should return true', () => {
  assert.equal(update("test-name"), "test-name")
})
  })
})


describe('mylogin', function() {
  // describes a module with nested "describe" functions
  describe('login', function() {
it('should return true', () => {
  assert.equal(mylogin("test"),"test" )
 })

it('should return true', () => {
  assert.equal(mylogin(""), "")
})

it('should return true', () => {
  assert.equal(mylogin(), null)
})
  })
})

describe('realtimetracker', function() {
  // describes a module with nested "describe" functions
  describe('add', function() {
it('should return true', () => {
  assert.equal(add("points"), true)
 })

it('should return true', () => {
  assert.equal(add("rebounds"), true)
})

it('should return true', () => {
  assert.equal(add("assists"), true)
})

 it('should return true', () => {
  assert.equal(add("turnovers"), true)
})

 it('should return true', () => {
  assert.equal(add("fouls"), true)
})
  })
})

describe('webrtc-patch', function() {
  // describes a module with nested "describe" functions
  describe('add', function() {
it('should return true', () => {
  assert.equal(webrtc-patch(), true)
 })

  })
})





