class Taka:
  @classmethod
  def this_is_a_class_method(cls):
    return cls.__name__

  def this_is_a_regular_method(self):
    return 'hi nothing to see here'

if __name__ == "__main__":
    print('Taka invokes class method:', Taka.this_is_a_class_method())
    # print('Taka invokes regular method:', Taka.this_is_a_regular_method())
    print()

    t = Taka()
    print('instance t invokes class method:', t.this_is_a_class_method())
    print('instance t invokes regular method:', t.this_is_a_regular_method())
