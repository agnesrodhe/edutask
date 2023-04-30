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

    // cy.get('form')
    //   .submit()

    // cy.get('img')
    //   .click()
  })

  // it('test test', () => {
  //   cy.get('h1')
  //     .should('contain.text', 'VideoTask')
  // })

  it('toggle is pressed, todo item is struck through', () => {
    // cy.get('li.todo-item')
    //   .get('span.checker')
    //   .click()
    //   .click()

    // cy.get('li.todo-item')
    //   .get('span.editable')

  })

  // it('when input field "title" is empty, the "Add" button should be disabled', () => {
  //   cy.get('.submit-form')
  //     .find('input[type=submit]')
  //     .should('be.disabled')
  // })

  // it('when input field "title" is not empty, the "Add" button should be enabled', () => {
  //   cy.get('.inputwrapper #title')
  //   .type('test@testande.com')

  //   cy.get('.submit-form')
  //     .find('input[type=submit]')
  //     .should('be.enabled')
  // })

  after(function () {
    cy.request({
      method: 'DELETE',
      url: `localhost:5001/users/${uid}`
    }).then((response) => {
      cy.log(response.body)
    })
  })

})