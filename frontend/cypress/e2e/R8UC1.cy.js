describe('testing R8UC1 add-button', () => {
  let uid
  let name
  let taskTitle

  before(function () {
    cy.fixture('user.json')
      .then((user) => {
        cy.request({
          method: 'POST',
          url: 'localhost:5001/users/create',
          form: true,
          body:user
        }).then((response) => {
          uid = response.body._id.$oid;
          name = user.firstName + ' ' + user.lastName;

          cy.fixture('task.json')
            .then((task) => {
              task["userid"] = uid;
              cy.request({
                  method: 'POST',
                  url: 'localhost:5001/tasks/create',
                  form: true,
                  body: task
              }).then((response) => {
                taskTitle = response.body[0].title;
              })
            })
        })
      })
    })

  beforeEach(function() {
    cy.visit('http://localhost:3000')

    cy.contains('div', 'Email Address')
      .find('input[type=text]')
      .type('test@testande.com')

    cy.get('form')
      .submit()

    cy.get('.container-element').eq(0)
      .find('a')
      .click()
  })

  it('when input field "title" is empty, the "Add" button should be disabled', () => {
    cy.get('.inline-form')
      .find('input[type=submit]')
      .should('be.disabled')
  })

  it('when input field "title" is not empty, the "Add" button should be enabled, new todo item is created and added to the bottom', () => {
    cy.viewport(1000, 800)

    cy.get('.inline-form')
      .find('input[type=text]')
      .type('test@testande.com')

    cy.get('.inline-form')
      .find('input[type=submit]')
      .should('be.enabled')

    cy.get('.inline-form')
      .find('input[type=submit]')
      .click()

    cy.get('.todo-item').eq(1)
      .find('.editable')
      .should('contain.text', 'test@testande.com')
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