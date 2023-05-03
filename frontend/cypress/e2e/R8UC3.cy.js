describe('R8UC3 testing item deletion', () => {
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
  
    it('If user clicks on the x symbol behind the description of the todo item, the todo item is deleted', () => {
      cy.get('.todo-item').eq(0)
        .find('span.remover')
        .click()
        
      cy.get('.todo-list')
        .should('not.have.class', 'todo-item')
        .and('have.length', 1)
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