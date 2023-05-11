describe('Logging into the system', () => {
  let uid
  let name

  before(function () {
    cy.fixture('user.json')
      .then((user) => {
        cy.request({
          method: 'POST',
          url: 'localhost:5001/users/create',
          form: true,
          body:user
        }).then((response) => {
          uid = response.body._id.$oid
          name = user.firstName + ' ' + user.lastName
        })
      })
  })
  beforeEach(function() {
    cy.visit('localhost:3000')
  })
  it('start on the landing page', () => {
    cy.get('h1')
      .should('contain.text', 'Login')
  })

  it('login to the system with an existing account', () => {
    cy.contains('div', 'Email Address')
      .find('input[type=text]')
      .type('test@testande.com')

    cy.get('form')
      .submit()

    cy.get('h1')
      .should('contain.text', 'Your tasks, ' + name)
  })

  after(function () {
    cy.request({
      method: 'DELETE',
      url: `localhost:5001/users/${uid}`
    }).then((response) => {
      cy.log(response.body)
    })
  })
})