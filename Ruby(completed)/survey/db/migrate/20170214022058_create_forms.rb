class CreateForms < ActiveRecord::Migration[5.0]
  def change
    create_table :forms do |t|
      t.string :name
      t.string :location
      t.string :language
      t.text :comment

      t.timestamps
    end
  end
end
