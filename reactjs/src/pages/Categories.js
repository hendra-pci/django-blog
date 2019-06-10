import React from 'react';
import {
  Card,
  CardHeader,
  CardBody } from 'reactstrap';
import Cookies from 'universal-cookie';
import axios from 'axios';
import Input from '../components/Input';

class Categories extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isTypedSlug: false,
      name: '',
      description: '',
      slug: '',
    }
    this.changeName = this.changeName.bind(this);
    this.changeDescription = this.changeDescription.bind(this);
    this.changeSlug = this.changeSlug.bind(this);
    this.submitForm = this.submitForm.bind(this);
  }

  componentDidMount() {
    document.title = 'Categories';
  }

  changeName(e) {
    this.setState({
      name: e.target.value,
    });

    if (!this.state.isTypedSlug) {
      this.setState({
        slug: e.target.value.slugify(),
      });
    }
  }

  changeDescription(e) {
    this.setState({
      description: e.target.value,
    });
  }

  changeSlug(e) {
    this.setState({
      slug: e.target.value,
    });
    if (!this.state.isTypedSlug) {
      this.setState({
        isTypedSlug: true,
      });
    }
  }

  submitForm(e) {
    e.preventDefault();
    const cookies = new Cookies();
    const csrftoken = cookies.get('csrftoken');
    const data = {
      name: this.state.name,
      description: this.state.description,
      slug: this.state.slug,
    };
    const self = this;
    // const mutation = `mutation createCategory($input: CreateCategoryInput!) {
    //   createCategory
    // }`
    axios({
      url: '/graphql',
      method: 'post',
      data: {
        variables: {
          "input": {
            "name": self.state.name,
            "description": self.state.description,
            "slug": self.state.slug,
            "parent": null,
            "language": null,
          }
        },
        query: `
          mutation createCategory($input: CreateCategoryInput!) {
            createCategory(input: $input) {
              id
              name
              description
              slug
              createdBy {
                id
                username
              }
            }
          }
        `
      }
    }).then((response) => {
      console.log(response.data);
    });
  }

  render() {
    return (
      <div className="container my-3">
        <div className="row">
          <div className="col col-lg-4 col-12">
            <Card>
              <CardHeader>
                <h5>New Category</h5>
              </CardHeader>
              <CardBody>
                <form method="POST" action="/graphql" onSubmit={this.submitForm} noValidate>
                  <Input name="name" label="Name" onChange={this.changeName} value={this.state.name} />
                  <Input name="description" label="Description" onChange={this.changeDescription} value={this.state.description} />
                  <Input name="slug" label="Slug" onChange={this.changeSlug} value={this.state.slug} />
                  <button type="submit" className="btn btn-success">Submit</button>
                </form>
              </CardBody>
            </Card>
          </div>
        </div>
      </div>
    );
  }
}

export default Categories;