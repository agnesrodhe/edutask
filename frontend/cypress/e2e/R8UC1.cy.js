describe('testing R8UC1 add-button', () => {
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
    
    // cy.fixture('task.json')
    //   .then((task) => {
    //     // const data = new URLSearchParams();
    //     // data.append('title', task["title"]);
    //     // data.append('userid', uid);
    //     // data.append('url', task["url"]);
    //     task["userid"] = uid
    //     // console.log(data)
    //     cy.request({
    //       method: 'POST',
    //       url: 'localhost:5001/tasks/create',
    //       // form: true,
    //       body:task
    //     })
    //   })
  })

  beforeEach(function() {
    cy.visit('localhost:3000')
    cy.contains('div', 'Email Address')
    .find('input[type=text]')
    .type('test@testande.com')

    cy.get('form')
      .submit()
  })

  it('start on the landing page', () => {
    cy.get('h1')
      .should('contain.text', 'Your tasks, Testa Testing')
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