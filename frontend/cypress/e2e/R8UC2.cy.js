describe('user click on icon', () => {
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
                })
            })
        })
      })  
    })

  beforeEach(function() {
    cy.visit('localhost:3000')

    cy.contains('div', 'Email Address')
    .find('input[type=text]')
    .type('test@testande.com')

    cy.get('form')
      .submit()

    cy.get('.container-element').eq(0)
      .find('a')
      .click()
  })

  it('toggle is pressed, todo item is struck through', () => {
    cy.get('li.todo-item')
      .get('span.checker')
      .click()

    cy.wait(500)

    cy.get('li.todo-item')
      .get('span.checker')
      .should('have.class', 'checked')

    cy.get('li.todo-item')
      .get('ul.todo-list > li.todo-item > span.checker.checked + span.editable')
      .should('have.css', 'text-decoration', 'line-through solid rgb(49, 46, 46)')
  })

  it('toggle is pressed, todo item is not struck through', () => {
    cy.get('li.todo-item')
      .get('span.checker')
      .click()

    cy.get('li.todo-item')
      .get('span.checker')
      .should('have.class', 'unchecked')

    cy.get('li.todo-item')
      .get('span.editable')
      .should('not.have.css', 'text-decoration', 'line-through solid rgb(49, 46, 46)')
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